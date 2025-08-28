from django import forms
from auths.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter email', 'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password', 'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
