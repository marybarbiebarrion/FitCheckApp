from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from datetime import date

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30, label="First Name")
    middle_name = forms.CharField(required=False, max_length=30, label="Middle Name")
    last_name = forms.CharField(required=True, max_length=30, label="Last Name")
    suffix = forms.CharField(required=False, max_length=10, label="Suffix")
    nickname = forms.CharField(required=False, max_length=30, label="Nickname")

    birthdate = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'text',  # Change from 'date' to 'text' to allow JS calendar picker
                'class': 'form-control flatpickr',
                'placeholder': 'MM/DD/YYYY',
            },
            format='%m/%d/%Y',
        ),
        input_formats=['%m/%d/%Y'],
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
        widget=forms.PasswordInput,
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
            'email', 'first_name', 'middle_name', 'last_name', 'suffix', 'nickname',
            'birthdate', 'sex_at_birth', 'password1', 'password2',
            'expression_of_consent', 'declaration_undertaking'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email address already exists. Please use a different email.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        birthdate = cleaned_data.get('birthdate')
        if birthdate and birthdate > date.today():
            self.add_error('birthdate', 'Birthdate cannot be in the future.')
        return cleaned_data

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn’t match.")

        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("Password must contain at least one number.")
        if not any(char.isalpha() for char in password1):
            raise forms.ValidationError("Password must contain at least one letter.")

        return password2

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'nickname', 'email', 'phone_number', 'address', 'country', 
            'region', 'province', 'municipality', 'city', 'address_block'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

# Health Profile Form (to allow the user to update their health information)
class HealthProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'height','weight','asthma', 'hypertension', 'thyroid_problem', 'acid_peptic_disorder',
            'convulsions_or_seizure', 'anxiety_mood_problems', 'depression', 
            'diabetes', 'g6pd_deficiency', 'tuberculosis', 'stroke_heart_disease', 
            'kidney_urinary_problems', 'recurrent_headaches', 'eating_problems', 
            'suicidal_thoughts', 'surgeries', 'covid_history', 'menstrual_problems', 
            'other_medical_conditions', 'diagnosis_date', 'illness_status', 
            'other_medications', 'smoker', 'alcohol_rate', 'alcohol_units_per_day',
            'psychoactive_substance', 'special_needs', 'medications_taken', 'allergies', 
            'allergy_name', 'allergy_severity'
        ]
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'illness_status': forms.Textarea(attrs={'rows': 2}),
            'other_medical_conditions': forms.Textarea(attrs={'rows': 3}),
            'other_medications': forms.Textarea(attrs={'rows': 3}),
            'medications_taken': forms.Textarea(attrs={'rows': 3}),
        }
