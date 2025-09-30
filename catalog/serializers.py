from rest_framework import serializers
from .models import Collection, Product, ProductImage, Accessory


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image", "order"]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "slug", "name", "description", "banner_image", "banner_video", "created_at"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    collection = CollectionSerializer(read_only=True)
    collection_id = serializers.PrimaryKeyRelatedField(source="collection", queryset=Collection.objects.all(), write_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "slug",
            "name",
            "price",
            "color",
            "material",
            "size",
            "description",
            "is_featured",
            "collection",
            "collection_id",
            "images",
            "created_at",
        ]


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ["id", "slug", "name", "price", "banner_image", "banner_video", "description", "created_at"]




