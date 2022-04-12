from django.urls import path

from apps.web.views import dashboard, changelog, servers

urlpatterns = [
    # Servers
    path('servers', servers.ServerManagement.as_view(), name='server-management'),

    path("changelog", changelog.Changelog.as_view(), name='changelog'),
    path("", dashboard.Dashboard.as_view(), name='dashboard'),
]
