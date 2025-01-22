from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisteSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            get_email = User.objects.get(email = email) 
        except User.DoesNotExist:
            return Response({'error': "Invalid Credentials"})
        
        authenticated_user = authenticate(username = get_email.username, password = password)

        if authenticated_user:
            login(request, authenticated_user)

            user_role = authenticated_user.role.role  # Access the role via related name          

            if user_role:
                role = 'admin'
            else:
                role = 'user'
            # Prepare user details
            user_data = {
                'id': str(authenticated_user.id),
                'full_name': f"{authenticated_user.first_name} {authenticated_user.last_name}",
                'email': authenticated_user.email,
                'role': role
            }
            
            refresh = RefreshToken.for_user(authenticated_user)
            # Prepare tokens
            tokens = {
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }
            return Response({'user': user_data, 'tokens': tokens}, status= status.HTTP_200_OK)
        else:
            return Response({'error': "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)