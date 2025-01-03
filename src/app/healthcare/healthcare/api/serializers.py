import json
from datetime import date

from rest_framework import serializers
from pydantic.v1.error_wrappers import ValidationError

from app.healthcare.healthcare.api import models


__all__ = ["PatientSerializer"]


class _DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)


class PatientSerializer(serializers.ModelSerializer):
    def validate(self, data):
        from fhir.resources.patient import Patient
        decoded_data = json.loads(json.dumps(data, cls=_DataEncoder))
        try:
            Patient.parse_obj(decoded_data)
        except ValidationError as err:
            raise serializers.ValidationError(str(err))

        return data

    class Meta:
        model = models.Patient
        fields = "__all__"
