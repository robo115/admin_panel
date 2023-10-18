from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Clients, Notifications, Filterwords
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser

TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)


class AddUserForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    tts_enabled = forms.ChoiceField(widget=forms.Select(), required=True, choices=TRUE_FALSE_CHOICES,
                                    label='Text-to-Speech setting')

    class Meta:
        model = Clients
        fields = ("username", "tts_enabled")


class NotificationForm(UserChangeForm):
    sms = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sms'}))
    whatsapp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Whatsapp'}))
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'comment'}))
    telegram = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telegram'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = Notifications
        fields = ("sms", "whatsapp", "comment", "telegram", "email")


class FilterWordsForm(UserChangeForm):
    word = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Word'}))
    wordalias = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Word alias'}))
    subwordalias = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sub word alias'}))
    stopword = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Stopword'}))

    class Meta:
        model = Filterwords
        fields = ("word", "wordalias", "subwordalias", "stopword")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name', 'class': 'form-control', 'autofocus': 'autofocus'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
       'class': 'form-control', 'placeholder': 'password'
    }))

    class Meta:
        model = AbstractUser
        fields = ('username', 'password')
