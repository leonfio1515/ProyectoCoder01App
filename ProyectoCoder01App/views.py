from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def VInicio(request):
    listaCursos = Cursos.objects.all()
    return render(request,"ProyectoCoder01App/inicio.html", {"cursos":listaCursos} )

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

    return render(request, "ProyectoCoder01App/contacto.html")

def VCursos(request):
    listacursos = Cursos.objects.all()
    return render(request, "ProyectoCoder01App/cursos.html", {"cursos": listacursos})

def VAlumnos(request):
    alum = Usuario.objects.filter(tipo_usuario="Alumno")
    return render(request, "ProyectoCoder01App/alumnos.html", {"alumnos":alum})

def VProfesores(request):
    prof = Usuario.objects.filter(tipo_usuario = "Profesor")
    return render(request, "ProyectoCoder01App/profesores.html", {"profesor":prof})

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
    return render(request, "ProyectoCoder01App/inscribirse.html")

def VBuscar(request):
    if request.method == "POST":
        
        busqueda_cursos = request.POST["nombre_curso"]
        cursos = Cursos.objects.filter(nombre_curso__icontains=busqueda_cursos )
    
    else:
        cursos = []

    return render(request, "ProyectoCoder01App/buscar.html",  {"curso_buscado":cursos})

def VNoticias(request):
    listanoticia = Noticias.objects.all()
    return render(request, "ProyectoCoder01App/noticias.html", {"listnoticias":listanoticia})