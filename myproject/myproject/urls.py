from django.contrib import admin
from django.urls import path
from django.urls import include
import shop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.home, name='home'),
    path('shop/', include('shop.urls')),
    path('accounts/', include('accounts.urls')), # 일반 로그인
    path('account/', include('allauth.urls')), # 소셜 로그인
]