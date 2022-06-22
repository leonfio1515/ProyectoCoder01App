from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def VInicio(request):
    listaCursos = Cursos.objects.all()
    return render(request,"inicio.html", {"cursos":listaCursos} )

def VContacto(request):

    if request.method == 'POST':

        contacto_formulario = request.POST

        msj = Contacto(
            nombre_contacto=contacto_formulario["nombre_contacto"],
            email_contacto=contacto_formulario["email_contacto"],
            tel_contacto=contacto_formulario["tel_contacto"],
            asunto_contacto=contacto_formulario["asunto_contacto"],
            mensaje_contacto=contacto_formulario["mensaje_contacto"],
        )
        msj.save()
        return redirect("inicio")

    return render(request, "contacto.html")

def VCursos(request):
    listacursos = Cursos.objects.all()
    return render(request, "cursos.html", {"cursos": listacursos})

def VAlumnos(request):
    alum = Usuario.objects.filter(tipo_usuario="Alumno")
    return render(request, "alumnos.html", {"alumnos":alum})

def VProfesores(request):
    prof = Usuario.objects.filter(tipo_usuario = "Profesor")
    return render(request, "profesores.html", {"profesor":prof})

def VInscribirse(request):
    
    if request.method == 'POST':

        info_formulario = request.POST

        users = Usuario(
            nombre_usuario=info_formulario["nombre_usuario"],
            apellido_usuario=info_formulario["apellido_usuario"],
            nombre_user=info_formulario["nombre_user"],
            email_usuario=info_formulario["email_usuario"],
            direccion_usuario=info_formulario["direccion_usuario"],
            tel_usuario=info_formulario["tel_usuario"],
            tipo_usuario=info_formulario["tipo_usuario"],
            curso_usuario=info_formulario["curso_usuario"],

        )
        users.save()
        return redirect("inicio")
    return render(request, "inscribirse.html")

def VNoticias(request):
    listanoticia = Noticias.objects.all()
    return render(request, "noticias.html", {"listnoticias":listanoticia})