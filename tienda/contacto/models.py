from django.db import models
 
# Create your models here.
class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mensaje = models.TextField()
 
    def __str__(self):
        return self.nombre
