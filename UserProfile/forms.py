from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=150, label="Username")
    first_name = forms.CharField(required=True, max_length=30, label="First Name")
    middle_name = forms.CharField(required=False, max_length=30, label="Middle Name")
    last_name = forms.CharField(required=True, max_length=30, label="Last Name")
    suffix = forms.CharField(required=False, max_length=10, label="Suffix")
    nickname = forms.CharField(required=False, max_length=30, label="Nickname")
    birthdate = forms.DateField(widget=forms.SelectDateWidget, label="Birthdate")
    sex_at_birth = forms.ChoiceField(choices=User.sex_at_birth_choices, label="Sex at Birth")
    email = forms.EmailField(required=True, label="Email Address")
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
            raise forms.ValidationError("A user with that username already exists.")  # Match this message in the test
        return username
    
    def clean_email(self):
        """
        Ensure the email is unique.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this Email Address already exists.")  # Match this message in the test
        return email

    def clean(self):
        """
        Custom validation for the form.
        """
        cleaned_data = super().clean()

        # Example: Add additional custom validation logic if needed
        # For instance, ensure birthdate is not in the future
        birthdate = cleaned_data.get('birthdate')
        if birthdate and birthdate > forms.DateField().to_python('today'):
            self.add_error('birthdate', 'Birthdate cannot be in the future.')

        return cleaned_data
