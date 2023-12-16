from rest_framework import serializers
from .models import Coffee, CoffeeBean

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('id', 'origin', 'name', 'is_hot', 'price', 'size', 'created_at', 'updated_at')

class CoffeeBeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeBean
        fields = ('id', 'origin', 'bean_name', 'region', 'grade', 'processiong_method',
                  'stock', 'date_receipt', 'price', 'aroma', 'flavor', 'acidity', 'texture',
                  'aftertastes', 'uniformity', 'balance', 'cleancup', 'sweetness', 'total_score',
                  'created_at', 'updated_at')