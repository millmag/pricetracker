

from django.urls import path, include
from . import views


from rest_framework_swagger.views import get_swagger_view

app_name = 'app'


urlpatterns = [
    path('', views.home, name='home'),
    path('categories', views.CategoryView.as_view(), name='categories'),
    path('products', views.ProductsView.as_view(), name='products'),
    path('pricetracker', views.PriceTrackerView.as_view(), name='pricetracker'),
    path('shops', views.ShopView.as_view(), name='shops'),
    path('search',views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]
