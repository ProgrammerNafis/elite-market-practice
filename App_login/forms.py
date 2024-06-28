from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user')

class SignUpForm(forms.ModelForm):
    class Meta:
        fields = ('email','password1','password2')

        