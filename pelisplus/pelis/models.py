from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre Usuario')
    correo = models.EmailField(max_length =254, verbose_name = 'Correo')
    password = models.CharField(max_length=20, verbose_name = 'password')
    edad = models.IntegerField(max_length=3, verbose_name = 'edad')

class Pelicula(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre Pelicula')
    categoria = models.CharField(max_length =254, verbose_name = 'Categoria Pelicula')
    descripcion = models.CharField(max_length=254, verbose_name = 'Descripcion Pelicula')
    duracion = models.IntegerField(max_length=20, verbose_name = 'Duracion Pelicula')
    estado = models.BooleanField(default=False, verbose_name = 'Estado Pelicula')
    estreno = models.DataField(verbose_name ='lanzamiento Pelicula')

class list_P_Favorita(models.Model):
    lista = models.CharField(max_length = 50, verbose_name = 'Nombre lista')
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre Pelicula')
    categoria = models.CharField(max_length =254, verbose_name = 'Categoria Pelicula')
    duracion = models.IntegerField(max_length=20, verbose_name = 'Duracion Pelicula')
    idPelicula = models.ForeignKey(Pelicula, null = True, on_delete = models.CASCADE)
    estreno = models.DataField(verbose_name ='Lanzamiento Pelicula')

class List_p_Vistas(models.Model):
    nombre = models.CharField(max_length = 50, verbose_name = 'Nombre pelicula')
    categoria = models.CharField(max_length =254, verbose_name = 'Categoria Pelicula')
    duracion = models.IntegerField(max_length=20, verbose_name = 'Duracion Pelicula')
    fecha = models.DataField(verbose_name ='Fecha Vista')
    idPeliculaFavorita = models.ForeignKey(list_P_Favorita, null = True, on_delete = models.CASCADE)