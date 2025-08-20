from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BirdType(models.Model):
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


class BirdOrder(models.Model):
    """Orden de las aves"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BirdFamily(models.Model):
    """Familia de aves"""
    name = models.CharField(max_length=100)
    order = models.ForeignKey(BirdOrder, on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("name", "order")

    def __str__(self):
        return f"{self.name} ({self.order.name})"


class BirdGenus(models.Model):
    """Género de aves"""
    name = models.CharField(max_length=100)
    family = models.ForeignKey(BirdFamily, on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("name", "family")

    def __str__(self):
        return f"{self.name} ({self.family.name})"


class BirdSpecies(models.Model):
    """Especie de ave"""
    common_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, unique=True)
    genus = models.ForeignKey(
        BirdGenus, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    bird_type = models.ForeignKey(
        BirdType, on_delete=models.PROTECT, null=True, blank=True)
    habitats = models.ManyToManyField(Habitat, null=True, blank=True)

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"


class BirdPhoto(models.Model):
    """Fotografía de un ave"""
    bird = models.ForeignKey(BirdSpecies, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="birds/photos/")
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de {self.bird.common_name}"


class BirdObservation(models.Model):
    """Registro de avistamiento (occurrence)"""
    bird = models.ForeignKey(BirdSpecies, on_delete=models.CASCADE)
    observer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    photos = models.ManyToManyField(BirdPhoto, blank=True)
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


class BirdDistributionMap(models.Model):
    """Mapa de distribución de un ave"""
    bird = models.ForeignKey(BirdSpecies, on_delete=models.CASCADE)
    map_image = models.ImageField(upload_to="birds/maps/")
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mapa de {self.bird.common_name}"
