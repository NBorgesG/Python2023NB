from django.db import models

# Create your models here.


class Usuario(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}    Contrasenia: {self.contrasenia}    Dirección: {self.direccion}    Telefono: {self.telefono}"
    nombre = models.CharField(max_length=60)
    contrasenia = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=30)

class Maquillaje(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}    Color: {self.color}    Precio: {self.precio}      "
    nombre = models.CharField(max_length=40)
    color = models.CharField(max_length=10)
    precio = models.IntegerField() 

class Accesorio(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre}    Color: {self.color}    Precio: {self.precio}"
    nombre = models.CharField(max_length=40)
    color = models.CharField(max_length=10)
    precio = models.IntegerField()

    