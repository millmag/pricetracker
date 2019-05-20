from .models import Category, Product, PriceTracker, Shop

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True, slug_field='cname')

    class Meta:
        model = Product
        fields = '__all__'


class PriceTrackerSerializer(serializers.ModelSerializer):
    pname = serializers.SlugRelatedField(
        read_only=True, slug_field='pname')
    sname = serializers.SlugRelatedField(
        read_only=True, slug_field='sname')

    class Meta:
        model = PriceTracker
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
