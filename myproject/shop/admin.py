from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Delivery)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Board)
admin.site.register(Comment)