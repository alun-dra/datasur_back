from rest_framework import routers
from django.urls import include, path

from app.views.modeView import ClienteView

journals_router = routers.SimpleRouter(trailing_slash=False)
journals_router.register(r'client', ClienteView, basename='re_cliente')




urlpatterns = [
    path('Cliente/', include(journals_router.urls)),


]