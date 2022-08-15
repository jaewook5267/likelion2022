from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<int:product_id>/detail/', views.detail, name="detail"),
    path('cart/', views.cart, name="cart"),
    path('<int:product_id>/add_cart/', views.add_cart, name="add_cart"),

    path('count_down/', views.count_down, name="count_down"),
    path('count_up/', views.count_up, name="count_up"),
]
