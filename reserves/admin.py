from django.contrib import admin
from .models import Reserve, ReservePhoto


class ReservePhotoInline(admin.TabularInline):
    """
    Inline para mostrar las fotos de la reserva dentro del admin de Reserve
    """
    model = ReservePhoto
    extra = 1  # Muestra un formulario extra vacío
    readonly_fields = ('uploaded_at',)
    fields = ('image', 'description', 'uploaded_at')


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    """
    Admin para el modelo Reserve
    """
    list_display = ('name', 'get_birds', 'latitude', 'longitude')
    search_fields = ('name', 'description')
    list_filter = ('birds',)
    inlines = [ReservePhotoInline]

    def get_birds(self, obj):
        """
        Muestra las aves asociadas a la reserva como una lista
        """
        return ", ".join([bird.common_name for bird in obj.birds.all()])
    get_birds.short_description = "Aves"


@admin.register(ReservePhoto)
class ReservePhotoAdmin(admin.ModelAdmin):
    """
    Admin para el modelo ReservePhoto
    """
    list_display = ('reserve', 'description', 'uploaded_at')
    search_fields = ('reserve__name', 'description')
    readonly_fields = ('uploaded_at',)
