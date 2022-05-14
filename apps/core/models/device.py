from django.db import models

from apps.core.models import Server
from apps.core.models.base import BaseModel
from apps.core.models.service import Service


class Device(BaseModel):
    class Meta:
        app_label = 'core'
        db_table = 'devices'
        default_permissions = ()
        unique_together = (
            ('ip_address', 'port')
        )

    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=255, null=False, unique=True)
    ip_address = models.GenericIPAddressField(null=False)
    port = models.PositiveSmallIntegerField(null=False)
    services = models.ManyToManyField(Service, db_table='device_services')

    def __str__(self) -> str:
        return f"{self.name} ({', '.join(self.services.all().values_list('name', flat=True))})"


__all__ = [
    'Device'
]
