from django.contrib import admin

from apps.core.models import Device, Service, Server

admin.site.register(Server)
admin.site.register(Device)
admin.site.register(Service)
