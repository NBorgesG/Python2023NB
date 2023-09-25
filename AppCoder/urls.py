from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('maquillajes/', maquillaje, name="Maquillajes"),
    path('accesorios/', accesorio, name="Accesorios"),
    path('usuarios/', usuario, name="Usuarios"),
    path("maquillajeFormulario/", maquillajeFormulario, name="maquiForm"),
    path("accesorioFormulario/", accesorioFormulario, name="accForm"),
    path("usuarioFormulario/", usuarioFormulario, name="userForm"),
    path("busquedaNombreMaquillaje/", busquedaNombreMaquillaje, name="buscarForm"),
    path("resultadosBusqueda/", resultadosBusqueda, name="resForm"),
]
