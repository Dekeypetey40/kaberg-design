from django.db import models
from django import forms
from django.core.validators import EmailValidator


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(validators=[EmailValidator()])
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
