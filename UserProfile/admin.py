from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Extend the default UserAdmin to include custom fields
class UserAdmin(BaseUserAdmin):
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'last_updated')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('date_joined',)

    # Fields to display in the admin detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'suffix', 'nickname', 'birthdate', 'sex_at_birth', 'email')}),
        ('Consent and Declarations', {'fields': ('expression_of_consent', 'declaration_undertaking')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),  # Removed 'last_updated'
    )

    # Mark 'last_updated' as read-only
    readonly_fields = ('last_updated',)

    # Fields to display when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'suffix', 'nickname', 'birthdate', 'sex_at_birth', 'expression_of_consent', 'declaration_undertaking'),
        }),
    )

# Register the custom User model with the custom UserAdmin
admin.site.register(User, UserAdmin)