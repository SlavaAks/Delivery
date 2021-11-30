from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response

from .serializers import OrderSerializer
from .models import *


class OrderCreate(APIView):
    def post(self, request):
        cart = Cart(request)
        print(request.data,request.user)
        data=request.data
        data['customer']=Customer.objects.get(user=request.user,)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            print(order)
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item.product,
                                         price=item.product.price,
                                         quantity=item.qty)
            # Очищаем корзину.
            cart.clear()
            return Response(serializer.data)
        else:
            order = OrderSerializer()
            return Response(serializer.data)
