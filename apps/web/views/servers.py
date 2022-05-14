import ipaddress
import time
from uuid import UUID

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import UpdateView
from zeroconf import Zeroconf, IPVersion, ServiceBrowser

from apps.core.models import Server
from apps.web.zeroconf import ZeroconfListener


class ServerOverview(LoginRequiredMixin, View):
    login_url = '/admin/login'

    def get(self, request):
        return render(
            request,
            'web/servers/management.html',
            context={
                'servers': Server.objects.all()
            }
        )


class ServerDetail(View):
    def get(self, request, pk: UUID):
        try:
            server = Server.objects.get(pk=pk)
        except Server.DoesNotExist:
            raise Http404(_('Server not found!'))

        zeroconf = Zeroconf(ip_version=IPVersion.All)
        listener = ZeroconfListener()
        browser = ServiceBrowser(zeroconf, "_nug-ghoul._tcp.local.", listener)
        devices = {}

        for device in server.devices.all():
            devices[device.name] = {
                'name': device.name,
                'port': device.port,
                'address': device.ip_address,
                'services': device.services.values_list('name', flat=True),
                'is_active': False,
                'pk': device.pk
            }

        time.sleep(2)

        for service in listener.services.values():
            devices[service.name] = devices.get(service.name, {}) | {
                'name': service.name,
                'port': service.port,
                'address': next(map(str, map(ipaddress.ip_address, service.addresses))),
                'services': service.properties[b'services'].decode().split(','),
                'is_active': True
            }

        return render(
            request,
            'web/servers/detail.html',
            context={
                'server': server,
                'devices': devices
            }
        )


class ServerUpdate(LoginRequiredMixin, UpdateView):
    model = Server
    fields = ['name', 'port', 'users']
    template_name = 'web/servers/update.html'


class ServerDelete(View):
    def get(self, request, pk: UUID):
        try:
            server = Server.objects.get(pk=pk)
        except Server.DoesNotExist:
            raise Http404(_('Server not found!'))

        server.delete()

        return redirect('server-management')


__all__ = [
    'ServerOverview',
    'ServerDetail',
    'ServerDelete'
]
