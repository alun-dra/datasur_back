from rest_framework import serializers
from app.models.model import Cliente, ComunaCiudadRegion, Empresas

class ComunaCiudadRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComunaCiudadRegion
        fields = ['comuna', 'ciudad', 'region']

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ['nombre', 'giroempresa', 'telefonoempresa']

class ClienteSerializer(serializers.ModelSerializer):
    empresa = EmpresasSerializer()
    comuna_ciudad_region = ComunaCiudadRegionSerializer()

    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'profesion', 'email', 'telefonocliente', 'empresa', 'comuna_ciudad_region']
