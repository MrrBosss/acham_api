from rest_framework import viewsets, permissions
from .models import StaticPage
from .serializers import StaticPageSerializer


class StaticPageViewSet(viewsets.ModelViewSet):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageSerializer
    permission_classes = [permissions.AllowAny]




