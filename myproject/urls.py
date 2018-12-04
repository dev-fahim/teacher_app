"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token

schema_view = get_swagger_view(title='App API')


urlpatterns = [
    re_path(r'^swagger/$', schema_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('rest_framework.urls', namespace='rest_framework')),
    path('app/', include('owners.api.urls', namespace='api_owner')),
    path('api/accounts/', include('rest_auth.urls')),
    path('api/accounts/register/', include('rest_auth.registration.urls')),
    re_path(r'^api/verify/', verify_jwt_token),
    re_path(r'^api/refresh/', refresh_jwt_token),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATICS_DIRS) \
              + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
