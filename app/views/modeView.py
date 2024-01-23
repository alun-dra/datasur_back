from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models.model import Cliente  
from app.serializer.modelSerializer import ClienteSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ClienteView(viewsets.GenericViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer  
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['GET'], url_path='all')
    def GetClient(self, request, *args, **kwargs):
        """
            @url: http://{{host}}:{{port}}/api/Client/client/all?page={{page}}&name={{nombre}}&empresa={{empresa_id}}
            @ejemplo: http://127.0.0.1:8000/api/Client/client/all?page=1&name=Juan&empresa=1
            @successful_response: HTTP 200 (OK)
            @description: obtiene a todos los clientes registrados en la base de datos, con opción de filtrar por nombre y empresa. 
        """
        nombre_buscado = request.query_params.get('name', None)
        empresa_id = request.query_params.get('empresa', None)

        queryset = Cliente.objects.all()
        
        if nombre_buscado is not None:
            queryset = queryset.filter(nombres__icontains=nombre_buscado)
        if empresa_id is not None:
            queryset = queryset.filter(empresa__id=empresa_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ClienteSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ClienteSerializer(queryset, many=True)
        return Response(serializer.data)
