from django.contrib import admin

from Universidad.Apps.TorneosOnline.models import *
# Register your models here.

admin.site.register(Torneo)
admin.site.register(Persona)
admin.site.register(Equipo)
admin.site.register(Grupo)