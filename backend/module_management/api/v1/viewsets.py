from rest_framework import authentication
from module_management.models import (
    Module,
    ModuleShare,
    Module,
    ModuleShare,
    Module,
    ModuleShare,
)
from .serializers import (
    ModuleSerializer,
    ModuleShareSerializer,
    ModuleSerializer,
    ModuleShareSerializer,
    ModuleSerializer,
    ModuleShareSerializer,
)
from rest_framework import viewsets


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Module.objects.all()


class ModuleShareViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleShareSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ModuleShare.objects.all()
