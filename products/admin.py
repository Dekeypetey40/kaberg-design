from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'category',
        'price',
        'rating',
        'stock',
        'image',
    )
    ordering = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)