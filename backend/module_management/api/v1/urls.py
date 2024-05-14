from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ModuleViewSet,
    ModuleShareViewSet,
    ModuleViewSet,
    ModuleShareViewSet,
    ModuleViewSet,
    ModuleShareViewSet,
    ModuleViewSet,
    ModuleShareViewSet,
)

router = DefaultRouter()
router.register("module", ModuleViewSet)
router.register("moduleshare", ModuleShareViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
