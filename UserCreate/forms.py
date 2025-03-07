from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=30)
    middle_name = forms.CharField(required=False, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    suffix = forms.CharField(required=False, max_length=10)
    nickname = forms.CharField(required=False, max_length=30)
    birthdate = forms.DateField(widget=forms.SelectDateWidget)
    sex_at_birth = forms.ChoiceField(choices=User.sex_at_birth_choices)
    email_address = forms.EmailField(required=True)
    expression_of_consent = forms.BooleanField(required=True, error_messages={
        'required': 'You must agree to share your health data.'
    })
    declaration_undertaking = forms.BooleanField(required=True, error_messages={
        'required': 'You must declare and undertake the accuracy of your information.'
    })

    class Meta:
        model = User
        fields = [
            'first_name', 'middle_name', 'last_name', 'suffix', 'nickname', 'birthdate', 
            'sex_at_birth', 'email_address', 'password1', 'password2',
            'expression_of_consent', 'declaration_undertaking'
        ]
