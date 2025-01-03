from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


__all__ = ["Patient"]


class Gender(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    OTHER = "other", _("Other")
    UNKNOWN = "unknown", _("Unknown")


class Patient(models.Model):
    """https://www.hl7.org/fhir/patient.html"""

    id = models.AutoField(primary_key=True)
    resourceType = models.CharField(max_length=10, null=False)
    name = ArrayField(models.JSONField(default=dict, null=False), null=False, size=3)
    birthDate = models.DateField(null=False)
    gender = models.CharField(choices=Gender.choices, default=Gender.UNKNOWN, max_length=50, null=True)
    address = ArrayField(models.JSONField(default=dict, null=False), null=False, size=3)
    telecom = ArrayField(models.JSONField(default=dict, null=False), null=False, size=3)
    active = models.BooleanField(default=True, null=True)
    deceasedBoolean = models.BooleanField(default=False, null=True)
    maritalStatus = models.JSONField(default=dict, null=True)
    multipleBirthInteger = models.IntegerField(default=1, null=True)
    photo = ArrayField(models.JSONField(default=dict, null=True), null=True, size=3)
    contact = ArrayField(models.JSONField(default=dict, null=True), null=True, size=3)
    communication = ArrayField(models.JSONField(default=dict, null=True), null=True, size=3)
    generalPractitioner = ArrayField(models.JSONField(default=dict, null=True), null=True, size=3)
    managingOrganization = models.JSONField(default=dict, null=True)
    link = ArrayField(models.JSONField(default=dict, null=True), null=True, size=3)
