from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    """
    Custom permission to allow access only to users with the admin role.
    """
    message = "You must be an admin to perform this action."

    def has_permission(self, request, view):
        # Ensure the user is authenticated and has an admin role
        return request.user.is_authenticated and hasattr(request.user, 'role') and request.user.role.role
