from django.urls import path

from apps.web.views import dashboard, changelog, servers

urlpatterns = [
    # Servers
    path('servers', servers.ServerOverview.as_view(), name='server-management'),
    path('server/<uuid:pk>/detail', servers.ServerDetail.as_view(), name='server-detail'),
    path('server/<uuid:pk>/update', servers.ServerUpdate.as_view(), name='server-update'),
    path('server/<uuid:pk>/delete', servers.ServerDelete.as_view(), name='server-delete'),

    path("changelog", changelog.Changelog.as_view(), name='changelog'),
    path("", dashboard.Dashboard.as_view(), name='dashboard'),
]
