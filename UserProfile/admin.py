from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_joined', 'last_updated')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal Info', {'fields': ('first_name', 'middle_name', 'last_name', 'suffix', 'nickname', 'birthdate', 'sex_at_birth', 'email')}),
        ('Consent and Declarations', {'fields': ('expression_of_consent', 'declaration_undertaking')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('last_updated',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'middle_name', 'last_name', 'suffix', 'nickname', 'birthdate', 'sex_at_birth', 'expression_of_consent', 'declaration_undertaking'),
        }),
    )

admin.site.register(User, UserAdmin)
