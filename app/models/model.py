from django.db import models

COMUNAS_CHOICES = [
    ('lo_barnechea','Lo Barnechea'),
    ('las_condes', 'Las Condes'),
    ('vitacura', 'Vitacura'),
    ('providencia', 'Providencia'),
    ('nunoa', 'Ñuñoa'),
    ('la_reina', 'La Reina'),
    ('penalolen', 'Peñalolen'),
    ('macul', 'Macul'),
    ('la_florida', 'La Florida'),
    ('puente_alto', 'Puente Alto'),
    ('recoleta', 'Recoleta')
    
]

CIUDADES_CHOICES = [
    ('algarrobo', 'Algarrobo'),
    ('santiago', 'Santiago'),
    ('antofagasta', 'Antofagasta'),
    ('calama', 'Calama'),
    ('puerto_montt', 'Puerto Montt'),
    ('valdivia', 'Valdivia')


]

REGIONES_CHOICES = [
    ('arrica_parinacota', 'Arrica Parinacota'),
    ('coquimbo', 'Coquimbo'),
    ('maule', 'Maule'),
    ('los_rios', 'Los Rios'),
    ('tarapaca', 'Tarapaca'),
    ('valparaiso', 'Valparaiso'),
    ('nuble', 'Ñuble'),
    ('los_lagos', 'Los Lagos'),
    ('metropolitana', 'Region Metropolitana'),
    ('bio_bio', 'Bio Bio'),
    ('aysen', 'Aysen'),
    ('araucania', 'Araucania'),
 
   
]

class ComunaCiudadRegion(models.Model):
    comuna = models.CharField(max_length=100, choices=COMUNAS_CHOICES)
    ciudad = models.CharField(max_length=100, choices=CIUDADES_CHOICES)
    region = models.CharField(max_length=100, choices=REGIONES_CHOICES)

    def __str__(self):
        return f"{self.get_comuna_display()}, {self.get_ciudad_display()}, {self.get_region_display()}"

class Empresas(models.Model):
    nombre = models.CharField(max_length=255)
    giroempresa = models.CharField(max_length=255)  
    telefonoempresa = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.giroempresa} {self.telefonoempresa}"


class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    profesion = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    telefonocliente = models.CharField(max_length=15)

    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    comuna_ciudad_region = models.ForeignKey(ComunaCiudadRegion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"





