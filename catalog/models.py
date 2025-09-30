from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Collection(TimestampedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    banner_image = models.ImageField(upload_to="collections/banners/", blank=True, null=True)
    banner_video = models.FileField(upload_to="collections/videos/", blank=True, null=True)

    def __str__(self):
        return self.name


class Product(TimestampedModel):
    collection = models.ForeignKey(Collection, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=100, blank=True)
    material = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]


class Accessory(TimestampedModel):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    banner_image = models.ImageField(upload_to="accessories/banners/", blank=True, null=True)
    banner_video = models.FileField(upload_to="accessories/videos/", blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name




