from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterFormStudent(UserCreationForm):
    email = forms.EmailField(label='Email-Id', required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserRegisterFormStartup(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, label='Hotel Name', required=True)
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'state', 'city', 'district', 'zip_code']


