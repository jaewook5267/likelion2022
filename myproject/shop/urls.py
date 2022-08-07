from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('<int:product_id>/detail/', views.detail, name="detail"),
]
