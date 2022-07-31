from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name="register"),
    path('unregister/', views.unregister, name="unregister"),
    path('modify/', views.modify, name="modify"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]