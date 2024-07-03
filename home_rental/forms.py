from django import forms
from .models import AddRentalHome
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddRentalHomeForm(forms.ModelForm):
    class Meta:
        model = AddRentalHome
        exclude = ['slug']


    widgets = {
            'Visiting_Start': forms.TimeInput(attrs={'type': 'time'}),
            'Visiting_End': forms.TimeInput(attrs={'type': 'time'}),
            'Gate_closing_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)