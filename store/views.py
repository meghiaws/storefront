from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Collection, OrderItem, Product, Review
from .serializers import CollectionSerializer, ProductListCreateSerializer, ProductDetailSerializer, ReviewSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').defer(
        'inventory', 'last_update')

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'create':
            return ProductListCreateSerializer
        else:
            return ProductDetailSerializer

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection cannot be deleted'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
