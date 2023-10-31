from django.db import models
from django.urls import reverse
from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.dispatch import receiver

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=150, null=True, unique=True)
    parent_category = models.ForeignKey(
        'self', related_name='sub_categories',
        on_delete=models.SET_NULL, null=True, blank=True
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
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=200, null=True, unique=True)
    description = models.TextField()
    stock = models.IntegerField(blank=False, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except ValueError:
            url = ''
        return url


class Favorites(models.Model):
    class Meta:
        verbose_name_plural = 'Favorites'

    user = models.ForeignKey(User, 
                             related_name='favorites',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                             related_name='favorites',
                             on_delete=models.CASCADE,
                             null=True,
                             )


    def __str__(self):
        return f'({self.user},favorites)'
