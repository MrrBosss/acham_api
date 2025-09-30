from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action in ["create", "retrieve", "list"]:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]




