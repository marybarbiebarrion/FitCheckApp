from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Primary Key
    user_id = models.AutoField(primary_key=True)  # Auto-generated unique ID

    # Personal Information
    first_name = models.CharField(max_length=30, null=False)
    middle_name = models.CharField(max_length=30, null=True, blank=True)  # Optional
    last_name = models.CharField(max_length=30, null=False)
    suffix = models.CharField(max_length=10, null=True, blank=True)  # Optional
    nickname = models.CharField(max_length=30, null=True, blank=True)  # Optional
    birthdate = models.DateField(null=False)
    sex_at_birth_choices = [('M', 'Male'), ('F', 'Female')]
    sex_at_birth = models.CharField(max_length=1, choices=sex_at_birth_choices, null=False)

    # Account Information
    email_address = models.EmailField(unique=True, null=False)  # Used as a unique identifier
    password = models.CharField(max_length=255, null=False)  # Will be hashed

    # Consent and Declarations
    expression_of_consent = models.BooleanField(default=False, null=False)  # Yes/No
    declaration_undertaking = models.BooleanField(default=False, null=False)  # Yes/No

    # Metadata
    last_updated = models.DateTimeField(auto_now=True, null=False)

    # Resolve conflict by adding related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email_address})"
