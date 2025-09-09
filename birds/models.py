from django.db import models
from django.conf import settings
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL


class IUCNRedListCategory(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Order(models.Model):
    """Orden de las aves"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Family(models.Model):
    """Familia de aves"""
    name = models.CharField(max_length=100)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("name", "order")

    def __str__(self):
        return f"{self.name} ({self.order.name})"


class Genus(models.Model):
    """Género de aves"""
    name = models.CharField(max_length=100)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("name", "family")

    def __str__(self):
        return f"{self.name} ({self.family.name})"


class Species(models.Model):
    """Especie de ave"""
    common_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, unique=True)
    iucn_red_list_category = models.ForeignKey(
        IUCNRedListCategory, on_delete=models.PROTECT, null=True, blank=True)
    genus = models.ForeignKey(
        Genus, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.common_name)
            slug = base_slug
            counter = 1
            while Species.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"


class Photo(models.Model):
    """Fotografía de un ave"""
    bird = models.ForeignKey(Species, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="birds/photos/")
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.bird.common_name}"
