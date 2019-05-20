from django.contrib import admin
from .models import Product, Category, Shop, PriceTracker

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product


class ShopAdmin(admin.ModelAdmin):
    class Meta:
        model = Shop


class PriceTrackerAdmin(admin.ModelAdmin):
    class Meta:
        model = PriceTracker


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(PriceTracker)
