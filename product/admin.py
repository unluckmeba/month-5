from django.contrib import admin
from product.models import Category, Product, Review

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)