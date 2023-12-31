from django.contrib import admin
from .models import Product, Category, Favorites

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


class FavoritesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorites, FavoritesAdmin)
