from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # quantity = serializers.IntegerField(min_value=0)
    class Meta:
        model = Product
        fields = '__all__'

