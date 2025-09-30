from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Collection, Product, ProductImage, Accessory
from .serializers import CollectionSerializer, ProductSerializer, ProductImageSerializer, AccessorySerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all().order_by("-created_at")
    serializer_class = CollectionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description", "slug"]
    ordering_fields = ["created_at", "name"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related("collection").prefetch_related("images").order_by("-created_at")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["collection", "is_featured", "color", "material", "size"]
    search_fields = ["name", "slug", "description", "collection__name"]
    ordering_fields = ["created_at", "price", "name"]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["order", "id"]


class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all().order_by("-created_at")
    serializer_class = AccessorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description", "slug"]
    ordering_fields = ["created_at", "name", "price"]




