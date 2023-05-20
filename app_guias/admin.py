from django.contrib import admin


from .models import Usuarios, Agentes, Cargas

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Agentes)
admin.site.register(Cargas)