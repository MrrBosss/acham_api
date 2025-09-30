from rest_framework import views, permissions
from rest_framework.response import Response
from catalog.models import Product, Collection, Accessory
from catalog.serializers import ProductSerializer, CollectionSerializer, AccessorySerializer


class SearchView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        q = request.query_params.get("q", "").strip()
        results = {"products": [], "collections": [], "accessories": []}
        if q:
            products = Product.objects.filter(name__icontains=q)[:10]
            collections = Collection.objects.filter(name__icontains=q)[:10]
            accessories = Accessory.objects.filter(name__icontains=q)[:10]
            results = {
                "products": ProductSerializer(products, many=True, context={"request": request}).data,
                "collections": CollectionSerializer(collections, many=True, context={"request": request}).data,
                "accessories": AccessorySerializer(accessories, many=True, context={"request": request}).data,
            }
        return Response({"query": q, "results": results})




