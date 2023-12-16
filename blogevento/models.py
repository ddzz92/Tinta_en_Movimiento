from django.db import models

# Create your models here.
class blog_evento(models.Model):
    title = models.CharField(max_length=30, verbose_name = 'Título')
    image = models.ImageField(verbose_name = 'Imagen')
    day = models.CharField(max_length=30, verbose_name = 'Día')
    location = models.CharField(max_length=40, verbose_name = 'Ubicación')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de modificación')

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title