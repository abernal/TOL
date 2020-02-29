from django.db import models

# Create your models here.

class Partido(models.Model):
	Tipo_partido = models.CharField(max_length= 50)
	Pais_partido = models.CharField(max_length= 50)
	Ciudad_partido = models.CharField(max_length= 50)
	Grupo_partido = models.CharField(max_length= 50)
	Equipo_Local_partido = models.CharField(max_length= 4)
	Equipo_Vesitante_partido = models.CharField(max_length= 4)
	Fecha_partido = models.DateField()
	Campo_partido = models.CharField(max_length= 50)
	Gol_Local_partido = models.CharField(max_length= 4)
	Gol_Visitante_partido = models.CharField(max_length= 4)
	Goleador_partido = models.CharField(max_length= 4)
	

class Resultado(models.Model):
	Torneo_Resultado = models.CharField(max_length=4) #foreigkey
	Fecha_Resultado = models.DateField()
	Equipo_Resultado = models.CharField(max_length=4) #foreinkey
	Posicion_resultado = models.CharField(max_length=50)
	Pj_resultado = models.CharField(max_length=3)
	Pg_resultado = models.CharField(max_length=3)
	Pe_resultado = models.CharField(max_length=3)
	Pp_resultado = models.CharField(max_length=3)
	Gf_resultado = models.CharField(max_length=3)
	Gc_resultado = models.CharField(max_length=3)
	Gd_resultado = models.CharField(max_length=3)
	Pt_resultado = models.CharField(max_length=3)

class Horario(models.Model):
	Torneo_Horario = models.CharField(max_length=4) #foreingkey
	Fecha_Partido = models.DateField()
	Hora_Partido = models.DateField()
	ESTADOS = (('L','Libre'), ('O','Ocupado'))
	Estado =models.CharField(max_length=1, choices=ESTADOS, default='L')


class Sancion(models.Model):
	#	Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
	#	Curso = models.ForeignKey(Curso,null=False, blank=False, on_delete=models.CASCADE)
	Fecha_Sancion = models.DateField()
	FechaMatricula = models.DateField(auto_now_add=True)
	TIPOS = (('A','Amarilla'), ('R','Roja'))
	Tipo =models.CharField(max_length=1, choices=TIPOS, default='A')

		
