from django.contrib import admin
from nucleo.models import Medico, Medicamento, Paciente, Cita, Compra, CompraMedicamento
# Register your models here.

admin.site.register(Medico)
admin.site.register(Medicamento)
admin.site.register(Paciente)
admin.site.register(Cita)
admin.site.register(Compra)
admin.site.register(CompraMedicamento)


