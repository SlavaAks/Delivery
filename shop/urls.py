"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mainapp.views import *
from cart.views import *
from orders.views import *
urlpatterns = [
    path('', api_user),
    path('admin/',admin.site.urls),
    path('categories/', ViewCatigories.as_view()),
    path('products/<str:slug_category>', ViewProducts.as_view()),
    path('cart/', ViewCart.as_view()),
    path('add_cart_product/<int:id_product>',AddCartProduct.as_view()),
    path('delete_cart_product/<int:id_cart_product>', DeleteCartProduct.as_view()),
    path('change_qty/', ChangeQty.as_view()),
    path('make_order/', OrderCreate.as_view()),
]
