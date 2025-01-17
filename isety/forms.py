from django import forms
from .models import Poste, Recommandation, Transport, Logement, Stage
from django.forms import ModelForm

from django.contrib.auth.forms import AuthenticationForm

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=150, label="username")
#     password = forms.CharField(widget=forms.PasswordInput, label="Password")
    

from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)


class EmailLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['username']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
        return email

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'form-input'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'form-input'}))
    photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'placeholder': 'Upload your photo', 'class': 'form-input'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-input'}))
    telnum = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-input'}))
    password1 = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'form-input', 'id': 'password'}))
    password2 = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password', 'class': 'form-input', 'id': 're_password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'photo', 'email', 'telnum', 'password1', 'password2']


class PosteForm(ModelForm):
    class Meta:
        model = Poste
        # Specify fields from the Poste model and its subclasses
        fields = "__all__"

class RecommandationForm(ModelForm):
    class Meta:
        model = Recommandation
        fields = "__all__"


class TransportForm(ModelForm):
    class Meta:
        model = Transport
        fields = "__all__"
        


class LogementForm(ModelForm):
    class Meta:
        model = Logement    
        fields = "__all__"


class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = "__all__"
