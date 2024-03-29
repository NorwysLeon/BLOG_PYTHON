from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('usuario/', crearusuario, name="crearusuario"),
    path('', inicio, name="inicio"),
    path('acercademi/', acerca_de_mi, name="acerca_de_mi"),
    path('blogs/', blogs, name="blogs"),
    path('crearblogs/', blogs, name="crearblog"),
    path('formBlog/',formBlog, name="formBlog"),
    path('register/', register, name="register"),
    path('busqueda/', busqueda, name="busqueda"),
    path('login/', login_usuario, name="login"),
    path('logout/', LogoutView.as_view() , name="logout"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
    path('buscar/', buscar, name="buscar"),
    path('leerblog/', leerblog, name="leerblog"),
    path('eliminarblog/<id>', eliminarblog, name="eliminarblog"),
    

]