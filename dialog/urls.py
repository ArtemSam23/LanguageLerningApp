"""dialog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unittest.mock import patch

from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


def patch_the_method(func):
    def inner(*args, **kwargs):
        with patch('rest_framework.permissions.IsAuthenticated.has_permission', return_value=True):
            response = func(*args, **kwargs)
        return response

    return inner


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    url='http://127.0.0.1:8000/',
    permission_classes=(permissions.AllowAny,)
)

# schema_view = patch_the_method(get_swagger_view(title='Some API'))
urlpatterns = [
    # path('', schema_view),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('dialog_app.urls')),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    re_path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    re_path(r'^auth/', include("djoser.urls.jwt")),
    path('', include('lessons.urls')),
    path('', include('user_profile.urls')),
    path('', include('rating_app.urls')),
]
