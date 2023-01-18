from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField
    contrasena=models.CharField(max_length=8)
    

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Blog(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=1000)
    autor=models.CharField(max_length=50)
    fecha=models.DateField()
    imagen=models.ImageField(upload_to="blog")
    

    def __str__(self):
        return f"{self.titulo} - {self.subtitulo} - {self.cuerpo} - {self.autor} - {self.fecha} - {self.imagen}"

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)



