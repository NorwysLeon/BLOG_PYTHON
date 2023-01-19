from django.contrib import admin
from .models import Usuario, Avatar, Blog, Profile

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Avatar)
admin.site.register(Blog)
admin.site.register(Profile)
