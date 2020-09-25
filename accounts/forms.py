from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Account

class RegistrationForm(UserCreationForm):
	username = forms.CharField(max_length=60, help_text='Required. Add a valid email address')

	class Meta:
		model = Account
		fields = ("username", "password1", "password2")
		

class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('username', 'password')

	def clean(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			if not authenticate(username=username, password=password):
				raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('username',)

	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use.' % username)
