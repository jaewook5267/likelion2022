from django.contrib import admin
from django.urls import path
from django.urls import include
import shop.views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.home, name='home'),
    path('shop/', include('shop.urls')),
    path('accounts/', include('accounts.urls')), # 계정 관리
    path('accounts/', include('allauth.urls')), # 소셜 로그인
]