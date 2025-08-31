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

class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username', 'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter phone', 'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter address', 'class':'form-control'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter bio', 'class':'form-control'}))

    class Meta:
        fields = ['username', 'phone', 'sddress', 'bio']

