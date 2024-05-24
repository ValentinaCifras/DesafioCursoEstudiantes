from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    version = models.IntegerField()

    def __str__(self):
        return f"Codigo Curso: {self.codigo} / Nombre: {self.nombre} / Version: {self.version}"

class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True, null=True, blank=True)
    modificacion_registro = models.DateField(auto_now_add=True, null=True, blank=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField("Curso", related_name="profesores")

    def __str__(self):
        return f"RUT: {self.rut} / Nombre: {self.nombre} / Apellido:{self.apellido}"

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True, null=True, blank=True)
    modificacion_registro = models.DateField(auto_now_add=True, null=True, blank=True)
    creado_por = models.CharField(max_length=50)
    curso = models.ManyToManyField("Curso", related_name="estudiantes")

    def __str__(self):
        return f"RUT: {self.rut} / Nombre:{self.nombre} / Apellido:{self.apellido}"

class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    depto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=10, null=False, blank=False) 
    ciudad = models.CharField(max_length=10, null=False, blank=False)
    region = models.CharField(max_length=10, null=False, blank=False)
    estudiante_id = models.OneToOneField('Estudiante', related_name='direccion', on_delete=models.CASCADE)

    def __str__(self):
        return f"Direccion: {self.calle} {self.numero} {self.depto} {self.ciudad}"
