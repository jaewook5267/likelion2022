from django.contrib import admin
from django.urls import path
from django.urls import include
import shop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.home, name='home'),
    path('shop/', include('shop.urls')),
    path('account/', include('account.urls')),
]