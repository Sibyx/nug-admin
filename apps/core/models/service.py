from django.db import models

from apps.core.models.base import BaseModel


class Service(BaseModel):
    class Meta:
        app_label = 'core'
        db_table = 'services'
        default_permissions = ()

    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


__all__ = [
    'Service'
]
