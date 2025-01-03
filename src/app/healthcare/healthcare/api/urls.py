from django.urls import include, path
from rest_framework import routers

from app.healthcare.healthcare.api import views


api_router = routers.DefaultRouter()
api_router.register(r"Patient", views.PatientViewSet, "Patient")

urlpatterns = [
    path("", include(api_router.urls)),
]
