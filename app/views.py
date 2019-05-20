"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Category, Product, PriceTracker, Shop
from .serializers import CategorySerializer, ProductSerializer, PriceTrackerSerializer, ShopSerializer
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from django.http import HttpResponse
from django.db.models.functions import Trim


def search(request):
    category = Category.objects.all()
    shop = Shop.objects.all()
    prod = Product.objects.all()

    searchme = request.GET['search']
    searchme = str(searchme.upper())
   
    
    product = Product.objects.filter(pname__contains = searchme)
    ptracker = PriceTracker.objects.all()
    allproducts = Product.objects.all()

    if not product:
        found = False
        return render(
            request, 
            'app/index.html', 
            {
                'found':found , 
                'product':product ,
                'category':category,
                'shop':shop,
                'prod':prod,
                'allproducts':allproducts
            }
        )
    else:
        print(searchme)
        print(product)
        found = True
        return render(
            request, 
            'app/index.html', 
            {
                'ptracker' : ptracker,
                'category':category,
                'shop':shop,
                'prod':prod,
                'product':product
            }
        )

def home(request):
    category = Category.objects.all()
    shop = Shop.objects.all()
    prod = Product.objects.all()
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'category':category,
            'shop':shop,
            'prod':prod,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

class CategoryView(APIView):
    def get(self, request):
        '''
        returns all product categories
        '''

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductsView(APIView):
    def get(self, request):
        '''
        returns all products 
        '''

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class PriceTrackerView(APIView):
    def get(self, request):
        '''
        returns pricetracker
        '''
        price_tracker = PriceTracker.objects.all()
        serializer = PriceTrackerSerializer(price_tracker, many=True)
        return Response(serializer.data)


class ShopView(APIView):
    def get(self, request):
        '''
        returns all shops
        '''
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)