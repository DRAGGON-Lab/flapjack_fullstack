from django.contrib import admin
from django.urls import include, path
from registry.health import HealthCheckView

urlpatterns = [
    path('', include('registry.urls')),
    path('api/auth/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls),
    path('api/healthz/', HealthCheckView.as_view(), name='healthz'),
]