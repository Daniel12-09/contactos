from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre