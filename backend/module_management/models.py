from django.conf import settings
from django.db import models


class Module(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    created_at = models.DateTimeField(
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        null=False,
        blank=False,
    )


class ModuleShare(models.Model):
    "Generated Model"
    module = models.ForeignKey(
        "module_management.Module",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="shared_modules",
    )
    shared_with = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="shared_modules",
    )


# Create your models here.
