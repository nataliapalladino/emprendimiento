from django.db import models
from django.core.validators import MinValueValidator

class Pijama(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre del pijama"
    )
    
    descripcion = models.TextField(
        verbose_name="Descripción",
        help_text="Describe las características del pijama"
    )
    
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Precio"
    )
    
    imagen = models.ImageField(
        upload_to='pijamas/',
        verbose_name="Imagen del pijama",
        help_text="Sube una imagen del pijama"
    )
    
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    
    disponible = models.BooleanField(
        default=True,
        verbose_name="Disponible"
    )

    class Meta:
        verbose_name = "Pijama"
        verbose_name_plural = "Pijamas"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre