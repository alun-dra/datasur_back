from rest_framework import routers
from django.urls import include, path

from app.views.modeView import ClienteView
from app.views.empresaView import EmpresasViewSet

client_router = routers.SimpleRouter(trailing_slash=False)
client_router.register(r'client', ClienteView, basename='re_cliente')

empre_router = routers.SimpleRouter(trailing_slash=False)
empre_router.register(r'empre', EmpresasViewSet, basename='re_empresa')




urlpatterns = [
    path('Client/', include(client_router.urls)),
    path('Empre/', include(empre_router.urls)),


]