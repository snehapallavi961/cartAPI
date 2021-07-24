from rest_framework import viewsets
from . import models
from . import serializers

class shoppingcartViewset(viewsets.ModelViewSet):
    queryset = models.shoppingcart.objects.all()
    serializer_class = serializers.shoppingcartSerializer