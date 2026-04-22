from django.contrib import admin
from django.urls import include, path

from .health import healthz

urlpatterns = [
    path('', include('registry.urls')),
    path('api/auth/', include('accounts.urls'), name='accounts'),
    path('healthz/', healthz, name='healthz'),
    path('admin/', admin.site.urls),
]
