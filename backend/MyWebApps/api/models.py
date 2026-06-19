from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    paginas = models.IntegerField()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=50, default='Estudiante')

    def __str__(self):
        return self.username