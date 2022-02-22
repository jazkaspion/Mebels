from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contacts', contacts, name='contacts'),
    path('catalog', catalog, name='catalog'),
    path('product', product, name='product'),
]