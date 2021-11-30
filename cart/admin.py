from django.contrib import admin

# Register your models here.
from django.contrib import admin
from cart.models import *
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['owner']

#admin.register(CartProduct)
