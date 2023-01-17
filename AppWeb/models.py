from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField
    contrasena=models.CharField(max_length=8)
    

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)



