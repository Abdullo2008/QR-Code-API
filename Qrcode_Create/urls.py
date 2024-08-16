from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Qrcode_Create import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="QR List Api",
        default_version='v1',
        description="QR demo Project",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="igamberdiyevabdullo3@gmail.com"),
        license=openapi.License(name="demo License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('qrapp.urls')),

    # Swagger
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name="swagger-swagger-ui"),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
