from rest_framework import serializers
from .models import shoppingcart

class shoppingcartSerializer(serializers.ModelSerializer):
    class Meta:
        model = shoppingcart
        fields = '__all__'