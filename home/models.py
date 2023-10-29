from django.db import models
from django import forms
from django.core.validators import EmailValidator


class ContactUs(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
