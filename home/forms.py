from django import forms
from .models import ContactUs
from django.core.validators import EmailValidator


class ContactUsForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
            ))
    email = forms.EmailField(label="Email Address")
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            ))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                }
            ))
    class Meta:
        model = ContactUs
        fields = '__all__'
