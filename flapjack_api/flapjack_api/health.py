import redis
from django.conf import settings
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def healthz(request):
    checks = {}
    overall_ok = True

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        checks["database"] = "ok"
    except Exception as exc:  # pragma: no cover
        checks["database"] = f"error: {exc}"
        overall_ok = False

    redis_host, redis_port = settings.REDIS_HOST, settings.REDIS_PORT
    try:
        client = redis.Redis(host=redis_host, port=redis_port, socket_connect_timeout=1)
        client.ping()
        checks["redis"] = "ok"
    except Exception as exc:  # pragma: no cover
        checks["redis"] = f"error: {exc}"
        overall_ok = False

    status_code = 200 if overall_ok else 503
    return JsonResponse({"status": "ok" if overall_ok else "error", "checks": checks}, status=status_code)
