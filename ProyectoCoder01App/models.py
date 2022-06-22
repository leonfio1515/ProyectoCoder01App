from django.db import models


# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    apellido_usuario = models.CharField(max_length=20)
    nombre_user = models.CharField(max_length=20)
    email_usuario = models.EmailField()
    tel_usuario = models.IntegerField()
    direccion_usuario = models.CharField(max_length=50)
    tipo_usuario = models.CharField(max_length=20)
    curso_usuario = models.CharField(max_length=20)
    foto_usuario = models.ImageField(blank='', default="", upload_to='images/')


class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=20)
    costo_curso = models.IntegerField()
    comision_curso = models.IntegerField()
    foto_curso = models.ImageField(blank='', default="", upload_to='images/')

class Noticias(models.Model):
    nombre_noticia = models.CharField(max_length=20)
    noticia = models.CharField(max_length=1500)
    descripcion_noticia = models.CharField(max_length=200)
    imagen_noticia = models.ImageField(
        blank='', default="", upload_to='images/')


class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=20)
    email_contacto = models.EmailField()
    tel_contacto = models.IntegerField()
    asunto_contacto = models.CharField(max_length=40)
    mensaje_contacto = models.CharField(max_length=500)
