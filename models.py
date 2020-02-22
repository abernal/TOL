from django.db import models

# Create your models here.

class Torneo(models.Model):
    id_torneo = models.CharField(max_length=8)
    nombre_torneo = models.CharField(max_length=50)
    tipo_torneo = models.CharField(max_length=50)
    inicio_torneo = models.DateField()
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')


class Persona(models.Model):
    ApellidoPaterno = models.CharField(max_length=50)
    ApellidoMaterno = models.CharField(max_length=50)
    Nombres = models.CharField(max_length=50)
    DNI= models.CharField(max_length=8)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')


    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()


class Equipo(models.Model):
    Nombre = models.CharField(max_length=50)
    Creditos = models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Creditos)


class Grupo(models.Model):
    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso.Nombre)