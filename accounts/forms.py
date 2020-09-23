from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account

class RegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=20, help_text='Enter Unique username')

    class Meta:
        model=Account
        fields=('username','password1','password2')