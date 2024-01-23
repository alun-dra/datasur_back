from django.contrib import admin

# Register your models here.
from app.models.model import Cliente, ComunaCiudadRegion, Empresas


admin.site.register(Cliente)
admin.site.register(ComunaCiudadRegion)
admin.site.register(Empresas)