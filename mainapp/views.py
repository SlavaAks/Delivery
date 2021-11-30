from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer,CategorySerializer,ProductSerializer
from django.contrib.auth.models import User
from .models import Category,Product

@api_view(['GET', 'POST'])
def api_user(request):
    print('ssss')
    print(request.data["username"])
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        print('ssss')
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,\
        status=status.HTTP_400_BAD_REQUEST)


class ViewCatigories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,
    #                 status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,
    #                 status=status.HTTP_400_BAD_REQUEST)


class ViewProducts(APIView):
    def get(self, request,*args,**kwargs):
        category=Category.objects.get(slug=kwargs['slug_category'])
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,
    #                 status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,
    #                 status=status.HTTP_400_BAD_REQUEST)

