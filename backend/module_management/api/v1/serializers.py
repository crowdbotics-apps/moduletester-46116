from rest_framework import serializers
from module_management.models import Module, ModuleShare, Module, ModuleShare


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class ModuleShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleShare
        fields = "__all__"
