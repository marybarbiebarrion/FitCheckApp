from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None  # Remove inherited username field

    user_id = models.AutoField(primary_key=True)

    # Personal Information
    first_name = models.CharField(max_length=30, null=False)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=False)
    suffix = models.CharField(max_length=10, null=True, blank=True)
    nickname = models.CharField(max_length=30, null=True, blank=True, default="User")  # Default value added
    birthdate = models.DateField(null=False)
    sex_at_birth_choices = [('M', 'Male'), ('F', 'Female')]
    sex_at_birth = models.CharField(max_length=1, choices=sex_at_birth_choices, null=False)

    # Email as unique identifier
    email = models.EmailField(unique=True, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Consent and Declarations
    expression_of_consent = models.BooleanField(default=False, null=False)
    declaration_undertaking = models.BooleanField(default=False, null=False)

    last_updated = models.DateTimeField(auto_now=True, null=False)

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
        return f"{self.first_name} {self.last_name} ({self.email})"

    def get_nickname(self):
        return self.nickname if self.nickname else "User"