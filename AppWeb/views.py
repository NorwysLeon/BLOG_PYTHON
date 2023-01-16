from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import RegistroUsuarioForm
 
# Create your views here.
def inicio(request):
    return render(request, "Home.html")

def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")

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
                return render (request, "loginexitoso.html", {"mensaje":f"Usuario {usu} logueado correctamemte"})
            else:
                return render(request, "login.html", {"form": form, "mensaje": "Usuario y/o contraseña incorrectos"})
        else:
            return render(request, "login.html", {"form": form, "mensaje": "Usuario  y/o contraseña incorrectos"})
       
    else:
        form=AuthenticationForm()
        return render (request,"login.html", {"form": form})