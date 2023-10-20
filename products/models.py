from django.db import models
from django.urls import reverse
from django import forms
from django.core.validators import EmailValidator

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=150, null=True, unique=True)
    parent_category = models.ForeignKey(
        'self', related_name='sub_categories',
        on_delete=models.SET_NULL, null=True
    )
    description = models.TextField(max_length=1500, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    def get_slug(self):
        return str(self.slug)
    
    def get_url(self):
        return reverse ('products_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, null=True, unique=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    stock = models.IntegerField(blank=False, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)