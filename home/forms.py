from django import forms
from .models import ContactUs
from django.core.validators import EmailValidator


class ContactUsForm(forms.Form):
    class Meta:
        model = ContactUs
        fields = '__all__'
