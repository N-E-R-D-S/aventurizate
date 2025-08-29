from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Type(models.Model):
    """Tipo de ave: endémica o migratoria"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Habitat(models.Model):
    """Hábitat donde se encuentra el ave"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


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
    type = models.ForeignKey(
        Type, on_delete=models.PROTECT, null=True, blank=True)
    habitats = models.ManyToManyField(Habitat, blank=True)

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


class Observation(models.Model):
    """Registro de avistamiento (occurrence)"""
    bird = models.ForeignKey(Species, on_delete=models.CASCADE)
    observer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    photos = models.ManyToManyField(Photo, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_observed = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=1)
    note = models.TextField(blank=True)
    gbif_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ["-date_observed"]

    def __str__(self):
        return f"{self.bird.common_name} observado el {self.date_observed}"


class DistributionMap(models.Model):
    """Mapa de distribución de un ave"""
    bird = models.ForeignKey(Species, on_delete=models.CASCADE)
    map_image = models.ImageField(upload_to="birds/maps/")
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mapa de {self.bird.common_name}"
