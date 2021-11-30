from rest_framework import serializers
from django.contrib.auth.models import User,Group
from .models import Cart,CartProduct
from mainapp.models import Customer



class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'

    @staticmethod
    def get_user(obj):
        if not (obj.user.first_name and obj.user.last_name):
            return obj.user.username
        return ' '.join([obj.user.first_name, obj.user.last_name])

class CartSerializer(serializers.ModelSerializer):

    products = CartProductSerializer(many=True)
    owner = CustomerSerializer()

    class Meta:
        model = Cart
        fields = '__all__'

