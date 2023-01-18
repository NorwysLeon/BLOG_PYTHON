from django.shortcuts import render
from .models import Usuario, Avatar, Blog
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegistroUsuarioForm, EditUsuarioForm, AvatarForm, crearBlog

from django.contrib.auth.decorators import login_required  #para vistas basadas en funciones def
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en class


# Create your views here.

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len (lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/Pordefecto.png"
    return avatar

def inicio(request):
    return render(request, "Home.html")

def Home(request):
    return render(request, "inicio.html")

@login_required
def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")

def blogs(request):
    return render(request, "blogs.html")

def formBlog(request):
    if request.method=="POST":
        form= crearBlog(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion["titulo"]
            subtitulo=informacion["subtitulo"]
            cuerpo=informacion["cuerpo"]
            autor=informacion["autor"]
            fecha=informacion["fecha"]
            imagen=informacion["imagen"]
            blog= Blog(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            blog.save()
            return render (request, "Home.html", {"mensaje": "Blog creado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "formBlog.html", {"form": form, "avatar": obtenerAvatar(request)})
    else:
        formulario=crearBlog()
        return render (request, "formBlog.html", {"form": formulario, "avatar": obtenerAvatar(request)})



@login_required
def crearusuario(requets):
    usuario= Usuario(nombre="Norwys", email="norwysleon@gmail.com", contrasena="12345")
    usuario.save()
    cadena_texto= f"Usuario {usuario.nombre} guardado exitosamente"
    return HttpResponse(cadena_texto)

def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render (request, "registerexitoso.html", {"mensaje": f"Usuario {username} fue creado exitosamente.!"})      
        else:
            return render (request, "register.html", {"form": form, "mensaje": "ERROR AL CREAR USUARIO!"})  
    else:
        form=RegistroUsuarioForm()
        return render (request, "register.html", {"form": form})

def login_usuario(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            contraseña=info["password"]
            usuario=authenticate(username=usu, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return render (request, "loginexitoso.html", {"mensaje":f"Usuario {usu} logueado correctamemte", "avatar": obtenerAvatar(request)})
            else:
                return render(request, "login.html", {"form": form, "mensaje": "Usuario y/o contraseña incorrectos", "avatar": obtenerAvatar(request) })
        else:
            return render(request, "login.html", {"form": form, "mensaje": "Usuario  y/o contraseña incorrectos", "avatar": obtenerAvatar(request)})
       
    else:
        form=AuthenticationForm()
        return render (request,"login.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=EditUsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=["first_name"]
            usuario.last_name=["last_name"]
            usuario.save()
            return render(request, "editarPerfilExitoso.html", {"mensaje": f"Usuario {usuario.username} editado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render (request, "editarPerfil.html", {"form": form, "nombreusuario": usuario.username, "avatar": obtenerAvatar(request)})
    else:
        form=EditUsuarioForm(instance=usuario)
        return render (request, "editarPerfil.html", {"form": form, "nombreusuario": usuario.username, "avatar": obtenerAvatar(request)})

def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppCoder/Home.html", {"mensaje":f"Avatar agregado correctamente"})
        else:
            return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user})


