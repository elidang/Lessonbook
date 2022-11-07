from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['pcode']

admin.site.register(Product,ProductAdmin)




