from django import forms
from django.contrib.auth.models import User
from . models import profile


class Userprofile(forms.ModelForm):

    class Meta:
        model = profile
        fields = ('name','email')

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()
    class Meta():
        model = User
        fields = ('username','password',)