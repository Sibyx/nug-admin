from django.db import models

from apps.core.models.base import BaseModel


class LogRecord(BaseModel):
    class Meta:
        app_label = 'core'
        db_table = 'logs'
        default_permissions = ()

    class Levels(models.IntegerChoices):
        EMERGENCY = 0
        ALERT = 1
        CRITICAL = 2
        ERROR = 3
        WARNING = 4
        NOTICE = 5
        INFO = 6
        DEBUG = 7

    host = models.CharField(max_length=255, null=False)
    level = models.SmallIntegerField(choices=Levels.choices, null=False)
    message = models.TextField(null=False)


__all__ = [
    'LogRecord'
]
