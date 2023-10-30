from django import forms
from .models import ContactUs
from django.core.validators import EmailValidator


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {'name': forms.TextInput(
            attrs={'class': 'form-control'}
            ), 'email': forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            ), 'subject': forms.TextInput(
            attrs={
                'class': 'form-control',
                }
            ), 'message': forms.Textarea(
            attrs={
                'class': 'form-control',
                }
            )}
