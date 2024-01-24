from rest_framework import viewsets, status
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models.model import Empresas
from app.serializer.modelSerializer import EmpresasSerializer
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['POST'], url_path='ingre')
    def createEmpre(self, request, *args, **kwargs):
        """
            @url: http://{{host}}:{{port}}/api/Empre/empre/ingre
            @successful_response: HTTP 200 (OK)
            @description: se crea una empresa nueva. 
        """
        serializer = EmpresasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['GET'], url_path='all')
    def GetAllEmpresas(self, request, *args, **kwargs):
        """
            @url: http://{{host}}:{{port}}/api/Empre/empre/all?page={{page}}&name={{nombre}}
            @ejemplo: http://127.0.0.1:8000/api/Empre/empre/all?page=1&name=EmpresaX
            @successful_response: HTTP 200 (OK)
            @description: Obtiene todas las empresas registradas en la base de datos, con opción de filtrar por nombre. 
        """
        nombre_buscado = request.query_params.get('name', None)

        queryset = Empresas.objects.all()

        if nombre_buscado is not None:
            queryset = queryset.filter(nombre__icontains=nombre_buscado)

        # Contar total de empresas
        total_empresas = queryset.count()

        # Contar cuántas empresas tienen el mismo giroempresa
        giroempresa_counts = queryset.values('giroempresa').annotate(total=Count('giroempresa')).order_by('giroempresa')

        # Convertir a un diccionario para fácil acceso en la respuesta
        giroempresa_counter = {item['giroempresa']: item['total'] for item in giroempresa_counts}

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = EmpresasSerializer(page, many=True)
            return self.get_paginated_response({
                'total_empresas': total_empresas,
                'giroempresa_counter': giroempresa_counter,
                'results': serializer.data
            })

        serializer = EmpresasSerializer(queryset, many=True)
        return Response({
            'total_empresas': total_empresas,
            'giroempresa_counter': giroempresa_counter,
            'results': serializer.data
        })
    
    @action(detail=False, methods=['DELETE'], url_path='delete')
    def destroyEmpre(self, request):
        """
            @url: http://{{host}}:{{port}}/api/Empre/empre/delete?name=NombreDeLaEmpresa
            @successful_response: HTTP 204 (No Content)
            @description: Elimina una empresa por el nombre.
        """
        nombre_empresa = request.query_params.get('name', None)

        if not nombre_empresa:
            return Response({'error': 'Nombre de empresa no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            empresa = Empresas.objects.get(nombre=nombre_empresa)
            empresa.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Empresas.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['PUT'], url_path='update')
    def updateEmpre(self, request):
        """
            @url: http://{{host}}:{{port}}/api/Empre/empre/update?name=NombreDeLaEmpresa
            @successful_response: HTTP 200 (OK)
            @description: Actualiza los datos de una empresa por el nombre.
        """
        nombre_empresa = request.query_params.get('name', None)

        if not nombre_empresa:
            return Response({'error': 'Nombre de empresa no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            empresa = Empresas.objects.get(nombre=nombre_empresa)
            serializer = EmpresasSerializer(empresa, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Empresas.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)




