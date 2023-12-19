from django.contrib import admin
from . models import Category, Item

# Registered models
admin.site.register(Category)
admin.site.register(Item)