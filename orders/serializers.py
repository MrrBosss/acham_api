from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "product", "name", "unit_price", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "country",
            "city",
            "address",
            "postal_code",
            "status",
            "total_amount",
            "items",
            "created_at",
        ]
        read_only_fields = ["status", "total_amount", "created_at"]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)
        total = 0
        for item in items_data:
            quantity = item.get("quantity", 1)
            unit_price = item["unit_price"]
            total += unit_price * quantity
            OrderItem.objects.create(order=order, **item)
        order.total_amount = total
        order.save()
        return order




