from django.contrib import admin
from .models import Product, Offer


class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class offerAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, offerAdmin)
admin.site.register(Product, productAdmin)