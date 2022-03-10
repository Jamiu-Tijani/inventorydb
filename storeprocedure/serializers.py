from rest_framework import serializers
from . import models

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = ['username','password','email']

class inventoryDataSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=68, write_only=True)
    class Meta:
        model = models.stock_inventory
        fields = ["username", "product_title","product_price", "product_description"]
