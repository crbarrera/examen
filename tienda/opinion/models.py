from django.db import models
 
# Create your models here.
class Comentario(models.Model):
    nombre = models.CharField(max_length=50)
    comentario = models.TextField()
 
    def __str__(self):
        return self.nombre