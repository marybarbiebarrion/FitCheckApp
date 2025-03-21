from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from datetime import datetime, date

class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        max_length=150,
        label="Username",
        error_messages={'required': 'Please enter a username.'}
    )
    first_name = forms.CharField(required=True, max_length=30, label="First Name")
    middle_name = forms.CharField(required=False, max_length=30, label="Middle Name")
    last_name = forms.CharField(required=True, max_length=30, label="Last Name")
    suffix = forms.CharField(required=False, max_length=10, label="Suffix")
    nickname = forms.CharField(required=False, max_length=30, label="Nickname")
    birthdate = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1900, datetime.now().year + 1)  # Dynamic year range
        ),
        label="Birthdate",
        error_messages={'required': 'Please select your birthdate.'}
    )
    sex_at_birth = forms.ChoiceField(choices=User.sex_at_birth_choices, label="Sex at Birth")
    email = forms.EmailField(
        required=True,
        label="Email Address",
        error_messages={'required': 'Please enter an email address.'}
    )
    password2 = forms.CharField(
        required=True,
        label="Password confirmation",
        error_messages={'required': 'The two password fields didn’t match.'}
    )
    expression_of_consent = forms.BooleanField(
        required=True,
        label="Consent to Share Health Data",
        error_messages={'required': 'You must agree to share your health data.'}
    )
    declaration_undertaking = forms.BooleanField(
        required=True,
        label="Declaration of Accuracy",
        error_messages={'required': 'You must declare and undertake the accuracy of your information.'}
    )

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'middle_name', 'last_name', 'suffix', 'nickname',
            'birthdate', 'sex_at_birth', 'email', 'password1', 'password2',
            'expression_of_consent', 'declaration_undertaking'
        ]

    def clean_username(self):
        """
        Ensure the username is unique.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("The username you entered is already taken. Please choose a different one.")
        return username
    
    def clean_email(self):
        """
        Ensure the email is unique.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email address already exists. Please use a different email.")
        return email

    def clean(self):
        """
        Custom validation for the form.
        """
        cleaned_data = super().clean()

        # Ensure birthdate is not in the future
        birthdate = cleaned_data.get('birthdate')
        if birthdate and birthdate > date.today():
            self.add_error('birthdate', 'Birthdate cannot be in the future.')

        return cleaned_data

    def clean_password2(self):
        """
        Validate password strength.
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn’t match.")

        # Example: Add custom password strength validation
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("Password must contain at least one number.")
        if not any(char.isalpha() for char in password1):
            raise forms.ValidationError("Password must contain at least one letter.")

        return password2
