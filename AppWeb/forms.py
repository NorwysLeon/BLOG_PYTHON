from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroUsuarioForm(UserCreationForm):
    email= forms.EmailField(label="Email Usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
  
    class Meta:
        model=User
        fields= ["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}

class EditUsuarioForm(UserCreationForm):
    nombre=forms.CharField(label="Modificar Nombre")
    imagen=forms.ImageField(label="Imagen")
    descripcion=forms.CharField()
    web=forms.URLField()
    email= forms.EmailField(label="Email Usuario") 
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
       
 
    class Meta:
        model=User
        fields= ["email", "password1", "password2", "first_name", "last_name"]
        help_texts= {k:"" for k in fields}

class crearBlog(forms.Form):
    titulo=forms.CharField(label= "T´tulo", max_length=50)
    subtitulo=forms.CharField(label= "Subtítulo", max_length=50)
    cuerpo=forms.CharField(label="Cuerpo", max_length=500)
    #autor=forms.CharField(label="Autor", max_length=50)
    #fecha=forms.DateField(label="Fecha")
    #imagen=forms.ImageField(label="Imagen")



class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    



