import time
from uuid import UUID

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.views import View
from zeroconf import Zeroconf, IPVersion, ZeroconfServiceTypes, ServiceBrowser

from apps.core.models import Server
from apps.web.zeroconf import ZeroconfListener


class ServerManagement(LoginRequiredMixin, View):
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
    def get(self, request, server_id: UUID):
        try:
            server = Server.objects.get(pk=server_id)
        except Server.DoesNotExist:
            raise Http404(_('Server not found!'))

        zeroconf = Zeroconf(ip_version=IPVersion.All)
        listener = ZeroconfListener()
        services = list(ZeroconfServiceTypes.find(zc=zeroconf))
        browser = ServiceBrowser(zeroconf, services, listener)

        time.sleep(2)
        print(listener.services)

        return render(
            request,
            'web/servers/detail.html',
            context={
                'server': server,
                'services': listener.services
            }
        )


class ServerDelete(View):
    def get(self, request, server_id: UUID):
        try:
            server = Server.objects.get(pk=server_id)
        except Server.DoesNotExist:
            raise Http404(_('Server not found!'))

        server.delete()

        return redirect('server-management')


__all__ = [
    'ServerManagement',
    'ServerDetail',
    'ServerDelete'
]
