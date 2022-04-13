from django.contrib import admin

from apps.core.models import Service, Server

admin.site.register(Server)
admin.site.register(Service)
