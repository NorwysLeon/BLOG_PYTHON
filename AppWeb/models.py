from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField
       
    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="avatars")
    descripcion=models.TextField()
    web=models.URLField()
    email=models.EmailField()
    password1=models.CharField(max_length=8)

    def __str__(self):
        return f"{self.nombre} - {self.email}"
   
class Blog(models.Model):
    #autor=models.CharField(max_length=50)
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=50)
    cuerpo=models.CharField(max_length=1000)
    #user=models.ForeignKey(User, on_delete=models.CASCADE)
    #fecha=models.DateField()
    #imagen=models.ImageField(upload_to="blog")
    
    def __str__(self):
        return f"{self.titulo} - {self.subtitulo} - {self.cuerpo}"

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)



