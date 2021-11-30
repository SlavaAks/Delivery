from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CartSerializer
from django.contrib.auth.models import User
from .models import Cart, CartProduct
from mainapp.models import Customer, Product


def get_cart(user):
    cart = Cart.objects.get(owner=Customer.objects.get(user=user), for_anonymous_user=False)
    return cart

# Create your views here.
class ViewCart(APIView):
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        print(request, args, kwargs)
        print(request.user)
        if request.user.is_authenticated:
            cart = get_cart(request.user)
            cart_serializer = CartSerializer(cart)
            return Response(cart_serializer.data)
        else:
            return Response({'detail': "Корзина пуста, добавьте продукт"}, status=status.HTTP_400_BAD_REQUEST)


class AddCartProduct(APIView):
    def get(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(id=kwargs['id_product'])
            cart_product, created = CartProduct.objects.get_or_create(
                user=Customer.objects.get(user=request.user),
                product=product,
                cart=get_cart(request.user))
            cart =get_cart(request.user)
            if created:
                cart.products.add(cart_product)
                cart.save()
                return Response({"detail": "Товар добавлен в корзину", "added": True})
            return Response({'detail': "Товар уже в корзине", "added": False}, status=status.HTTP_400_BAD_REQUEST)
        except(Exception):
            return Response({'detail': "Нет такого продукта"}, status=status.HTTP_400_BAD_REQUEST)

class DeleteCartProduct(APIView):
    def get(self, request, *args, **kwargs):
        try:
            crproduct = CartProduct.objects.get(id=kwargs['id_cart_product'])
            cart =get_cart(request.user)
            cart.products.remove(crproduct)
            crproduct.delete()
            cart.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except(Exception):
            return Response({'detail': "Нет продукта в корзине"}, status=status.HTTP_400_BAD_REQUEST)

class ChangeQty(APIView):
    def patch(self,request, *args, **kwargs):
        data=request.data
        try:
            cart_product = CartProduct.objects.get(id=data['cart_product_id'])
            cart_product.qty = int(data['qty'])
            cart_product.save()
            cart_product.cart.save()
            return Response(status=status.HTTP_200_OK)
        except(Exception):
            return Response({'detail': "Нет продукта в корзине"}, status=status.HTTP_400_BAD_REQUEST)
