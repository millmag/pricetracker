"""
Definition of urls for pricetracker.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="PriceTracker API Documentation")

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('app/', include('app.urls', namespace='app')),
    
    path('docs/', schema_view, name='schema_view'),
]

    

    