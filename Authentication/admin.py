from django.contrib import admin
from django.contrib.auth.models import User
from .models import Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')  # Display fields in the admin list view
    list_filter = ('role',)  # Filter by role

    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = 'First Name'

    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = 'Last Name'

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email'


admin.site.register(Role, RoleAdmin)
