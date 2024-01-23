from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models.model import Empresas
from app.serializer.modelSerializer import EmpresasSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer


    @action(detail=False, methods=['GET'], url_path='ingre')
    def create(self, request, *args, **kwargs):
        """
            @url: http://{{host}}:{{port}}/api/Empre/empre/ingre
            @successful_response: HTTP 200 (OK)
            @description: obtiene a todos los clientes registrados en la base de datos, con opción de filtrar por nombre y empresa. 
        """
        serializer = EmpresasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['GET'], url_path='delete')
    def destroy(self, request, pk=None):
        """
            @url: http://{{host}}:{{port}}/api/Empre/empre/delete
            @successful_response: HTTP 200 (OK)
            @description: obtiene a todos los clientes registrados en la base de datos, con opción de filtrar por nombre y empresa. 
        """
        try:
            empresa = Empresas.objects.get(pk=pk)
            empresa.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Empresas.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    




