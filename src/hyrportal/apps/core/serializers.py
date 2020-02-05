from .models import User, WooCustomer, WooOrder, WooProduct
from rest_framework import serializers

class UserSerialzer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = '__all__'


class OrderSerialzer(serializers.ModelSerializer):

    class Meta:
        model = WooOrder
        fields = '__all__'



class ProductSerialzer(serializers.ModelSerializer):

    class Meta:
        model = WooProduct
        fields = '__all__'


class CustomerSerialzer(serializers.ModelSerializer):

    class Meta:
        model = WooCustomer
        fields = '__all__'
