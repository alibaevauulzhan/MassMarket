from django.contrib import admin
from .models import Product, Comment, Favorite

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Favorite)
