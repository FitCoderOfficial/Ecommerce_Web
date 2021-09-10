from django.urls import path, include
from .views import (ItemDetailView, products, checkout, HomeView)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView, name='product'),
]