from django.db import models

# Create your models here.

class Torneo(models.Model):
	Nombre_torneo = models.CharField(max_length= 50)
	Tipo_torneo = models.CharField(max_length= 50)
	Pais_torneo = models.CharField(max_length= 50)
	Ciudad_torneo = models.CharField(max_length= 50)
	Direccion_torneo = models.CharField(max_length= 50)
	Zona_torneo = models.CharField(max_length= 50)
	Inscritos_torneo = models.CharField(max_length= 4)
	Categoria_torneo = models.CharField(max_length= 50)
	Inicio_torneo = models.DateField()
	Fin_torneo = models.DateField()
	Primer_torneo = models.CharField(max_length= 8)
	Segundo_torneo = models.CharField(max_length= 8)
	Tercero_torneo = models.CharField(max_length= 8)
	Cuarto_torneo = models.CharField(max_length= 8)
	Goleador_torneo = models.CharField(max_length= 4)
	Guante_torneo = models.CharField(max_length= 4)
	Caracteristica_torneo = models.CharField(max_length= 200)


class Equipo(models.Model):
	Nombre_Equipo = models.CharField(max_length=50)
	Pais_Equipo = models.CharField(max_length=50)
	Ciudad_Equipo = models.CharField(max_length=50)
	Escudo_Equipo = models.CharField(max_length=50)
	Dueno_Equipo = models.CharField(max_length=50)
	Direccion_Equipo = models.CharField(max_length=50)
	Uniforme_Equipo = models.CharField(max_length=50)
	Telefono_Equipo = models.CharField(max_length=8)
	Descripcion_Equipo = models.CharField(max_length=200)

	
class Grupo(models.Model):
	Nombre_Grupo = models.CharField(max_length=50)
	Torneo_Grupo = models.PositiveIntegerField()
	Estado_Grupo = models.BooleanField(default=True)
	Nombre_Equipo1 = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
	#Nombre_Equipo2 = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
	#Nombre_Equipo3 = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
	#Nombre_Equipo4 = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)

	
class Deporte(models.Model):
	Nombre_Deporte = models.CharField(max_length=50)
	TIPOS = (('I','Individual'), ('G','Grupal'))
	Tipo_Deporte =models.CharField(max_length=1, choices=TIPOS, default='G')
	Cantidad_Deporte = models.CharField(max_length=2)

