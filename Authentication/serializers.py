from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role

class RegisteSerializer(serializers.ModelSerializer):
    role = serializers.BooleanField(write_only=True, required=False, default=None)
    confirm_password = serializers.CharField(required = True)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','confirm_password' , 'role')

    def save(self):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        role = self.validated_data['role']

        if password != confirm_password:
            raise serializers.ValidationError({'error': "Password Doesn't Matched"})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': "Email Already exits"})
        
        # Custom username generation based on email
        username = email.split('@')[0]
        
        account = User(first_name = first_name, last_name = last_name, email = email,username=username)
        account.set_password(password)
        account.save()
        Role.objects.create(user=account, role=role)

        return account
    
