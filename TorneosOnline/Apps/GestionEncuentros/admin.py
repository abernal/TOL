from django.contrib import admin
from TorneosOnline.Apps.GestionEncuentros.models import *

# Register your models here.

admin.site.register(Partido)
admin.site.register(Resultado)
admin.site.register(Horario)
admin.site.register(Sancion)