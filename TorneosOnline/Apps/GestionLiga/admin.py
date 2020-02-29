from django.contrib import admin
from TorneosOnline.Apps.GestionLiga.models import *
# Register your models here.

admin.site.register(Torneo)
admin.site.register(Equipo)
admin.site.register(Grupo)
admin.site.register(Deporte)