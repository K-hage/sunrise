import djoser.urls
from django.contrib import admin
from django.urls import (
    include,
    path
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/', include('corp.urls')),

    # swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
