from django.contrib import admin
from .models import Collection, Product, ProductImage, Accessory


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "collection", "is_featured", "created_at")
    list_filter = ("collection", "is_featured")
    search_fields = ("name", "slug")
    inlines = [ProductImageInline]


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "created_at")
    search_fields = ("name", "slug")




