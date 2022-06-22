from django.contrib import admin
from .models import*
# Register your models here.

class CursosAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_curso", 
        "costo_curso", 
        "comision_curso"
        )
    search_fields = (
        "nombre_curso",
        "costo_curso",
        "comision_curso"
        )

class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_usuario", 
        "apellido_usuario",
        "nombre_user", 
        "email_usuario", 
        "tel_usuario", 
        "direccion_usuario", 
        "tipo_usuario",
        )

    search_fields = (
        "nombre_usuario",
        "apellido_usuario",
        "nombre_user",
        "email_usuario",
        "tel_usuario",
        "direccion_usuario",
        "tipo_usuario",
    )


class NoticiasAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_noticia", 
        "noticia", 
        "descripcion_noticia", 
        "imagen_noticia"
        )
    search_fields = (
        "nombre_noticia", 
        "noticia",
        "descripcion_noticia"
        )


class ContactoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_contacto", 
        "email_contacto",
        "tel_contacto",
        "asunto_contacto",
        "mensaje_contacto",
        )
    search_fields = (
        "nombre_contacto",
        "email_contacto",
        "tel_contacto",
        "asunto_contacto",
        "mensaje_contacto",
    )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Cursos, CursosAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Contacto, ContactoAdmin)
