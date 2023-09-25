from django.shortcuts import render
from AppCoder.models import Maquillaje, Accesorio , Usuario
from AppCoder.forms import MaquillajeFormulario, AccesorioFormulario, UsuarioFormulario
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")

def maquillaje(request):
    return render(request,"AppCoder/maquillajes.html")

def accesorio(request):
    return render(request,"AppCoder/accesorios.html")

def usuario(request):
    return render(request,"AppCoder/usuarios.html")

def maquillajeFormulario(request):
    if request.method == "POST":

        formulario1= MaquillajeFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data
            maquillaje = Maquillaje(nombre=info["nombre"],color=info["color"],precio=info["precio"])
            maquillaje.save()
            return render (request, "AppCoder/inicio.html")
    else:
        formulario1 = MaquillajeFormulario()     
    return render(request, "AppCoder/maquillajeFormulario.html", {"formMaq":formulario1})

def accesorioFormulario(request):
    if request.method == "POST":

        formulario2= AccesorioFormulario(request.POST)

        if formulario2.is_valid():
            info = formulario2.cleaned_data
            accesorio = Accesorio(nombre=info["nombre"],color=info["color"],precio=info["precio"])
            accesorio.save()
            return render (request, "AppCoder/inicio.html")
    else:
        formulario2 = AccesorioFormulario()    
    return render(request, "AppCoder/accesorioFormulario.html", {"formAcc":formulario2})

def usuarioFormulario(request):
    if request.method == "POST":

        formulario3= UsuarioFormulario(request.POST)

        if formulario3.is_valid():
            info = formulario3.cleaned_data
            usuario = Usuario(nombre=info["nombre"],contrasenia=info["contrasenia"],direccion=info["direccion"],telefono=info["telefono"])
            usuario.save()
            return render (request, "AppCoder/inicio.html")
    else:
        formulario3 = UsuarioFormulario()    
    return render(request, "AppCoder/usuarioFormulario.html",{"formUser":formulario3})

def busquedaNombreMaquillaje(request):
    return render(request, "AppCoder/inicio.html")

def resultadosBusqueda(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        listaMaquillajes = Maquillaje.objects.filter(nombre__iexact=nombre)

        return render(request, "AppCoder/inicio.html", {"listaMaquillajes":listaMaquillajes, "nombre": nombre})
    else:
        respuesta = "No enviaste Datos"
    return HttpResponse(respuesta)


