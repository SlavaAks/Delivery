from rest_framework import serializers
from django.contrib.auth.models import User,Group
from .models import Category,Product
from cart.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('email','username', 'password','groups')
        fields = ('email', 'username', 'password')
    def create(self,validated_data):
        user=User(
            email=validated_data['email'],
            username=validated_data['username'],

        )
        group = Group.objects.filter(pk=validated_data['groups'])
        print(*group)
        user.groups.add(*group)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


# class CustomCategorySerializer(CategorySerializer):
#
#     products = serializers.SerializerMethodField()
#
#     @staticmethod
#     def get_products(obj):
#         return ProductSerializer(Product.objects.filter(category=obj), many=True).data


class CartProductSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'qty', 'final_price']
