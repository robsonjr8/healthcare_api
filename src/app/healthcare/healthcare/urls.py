"""
URL configuration for healthcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly


schema_view = get_schema_view(
    openapi.Info(
        title="Healthcare API",
        default_version="0.1.0",
        description="API documentation"
    ),
    public=True,
    permission_classes=[IsAuthenticatedOrReadOnly]
)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("accounts/profile/", RedirectView.as_view(url='/api/v1/docs/', permanent=False)),
    path("fhir/", include("app.healthcare.healthcare.api.urls")),
    path("api/v1/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-schema"),
]
