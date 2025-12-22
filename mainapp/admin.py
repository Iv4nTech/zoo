from django.contrib import admin
from .models import Animal,Consulta,Especie,Recinto,Vacuna,Veterinario, VacunaAnimal

admin.site.register(Animal)
admin.site.register(Consulta)
admin.site.register(Especie)
admin.site.register(Recinto)
admin.site.register(Vacuna)
admin.site.register(Veterinario)
admin.site.register(VacunaAnimal)