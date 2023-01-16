from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField
    contrasena=models.CharField(max_length=8)

    def __str__(self):
        return f"{self.nombre} - {self.email}"
