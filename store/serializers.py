from decimal import Decimal
from django.db.models import fields
from rest_framework import serializers
from .models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description',
                  'price', 'tax', 'collection']

    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    tax = serializers.SerializerMethodField(method_name="calculate_tax")
    collection = serializers.StringRelatedField(read_only=True)

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description',
                  'price', 'tax', 'collection']

    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    tax = serializers.SerializerMethodField(method_name="calculate_tax")
    collection = CollectionSerializer()

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
