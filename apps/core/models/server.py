from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from apps.core.models.base import BaseModel


class Server(BaseModel):
    class Meta:
        app_label = 'core'
        db_table = 'servers'
        default_permissions = ()

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    name = models.SlugField(max_length=200)
    port = models.PositiveSmallIntegerField(null=False, unique=True)
    users = models.ManyToManyField(User, db_table='user_servers', related_name='servers')

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('server-detail', kwargs={'pk': self.pk})


__all__ = [
    'Server'
]
