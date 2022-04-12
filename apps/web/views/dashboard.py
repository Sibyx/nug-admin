from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class Dashboard(LoginRequiredMixin, View):
    login_url = '/admin/login'

    def get(self, request):
        return render(request, 'web/dashboard.html')


__all__ = [
    'Dashboard',
]
