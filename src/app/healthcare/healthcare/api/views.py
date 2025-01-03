from rest_framework import permissions, viewsets

from app.healthcare.healthcare.api.serializers import PatientSerializer
from app.healthcare.healthcare.api.models import Patient


__all__ = ["PatientViewSet"]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by("name")
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
