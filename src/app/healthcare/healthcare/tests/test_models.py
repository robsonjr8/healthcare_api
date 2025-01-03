import copy
import datetime

from django.test import TestCase

from app.healthcare.healthcare.api.models import Patient
from app.healthcare.healthcare.tests.test_setup import PAYLOAD


class TestPatient(TestCase):
    def test_create_object(self):
        payload = copy.deepcopy(PAYLOAD)
        new_patient = Patient.objects.create(**payload)
        self.assertEqual(new_patient.address, [{'city': 'My City', 'state': 'My State', 'postalCode': '1234-000'}])
        self.assertEqual(new_patient.birthDate, "2000-01-01")
        self.assertEqual(new_patient.gender, "male")
        self.assertEqual(new_patient.name, [{'family': 'Surname', 'given': ['First Name']}])
        self.assertEqual(new_patient.resourceType, "Patient")
        self.assertEqual(new_patient.telecom, [{'system': 'email', 'value': 'patient@mail.com'}])

    def test_create_object_communication_field(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["communication"] = [
            {
                "language": {
                    "coding": [
                        {
                            "system": "urn:ietf:bcp:47",
                            "code": "nl-NL",
                            "display": "Dutch"
                        }
                    ]
                },
                "preferred": True,
            }
        ]
        new_patient = Patient.objects.create(**payload)
        self.assertTrue(new_patient.communication[0]["preferred"])

    def test_update_object_using_save_object_method(self):
        payload = copy.deepcopy(PAYLOAD)
        new_patient = Patient.objects.create(**payload)
        new_patient.birthDate = "2000-12-31"
        new_patient.save()
        self.assertEqual(new_patient.address, [{'city': 'My City', 'state': 'My State', 'postalCode': '1234-000'}])
        self.assertEqual(new_patient.birthDate, "2000-12-31")
        self.assertEqual(new_patient.gender, "male")
        self.assertEqual(new_patient.name, [{'family': 'Surname', 'given': ['First Name']}])
        self.assertEqual(new_patient.resourceType, "Patient")
        self.assertEqual(new_patient.telecom, [{'system': 'email', 'value': 'patient@mail.com'}])

    def test_update_object_using_update_model_methodwhen_specifying_a_non_existing_id_returns_zero(self):
        update_status: int = Patient.objects.filter(id=0).update(**{"birthDate": "2010-01-01"})
        self.assertEqual(update_status, 0)

    def test_update_object_using_update_model_methodwhen_specifying_an_existing_id_updates_successfully(self):
        payload = copy.deepcopy(PAYLOAD)
        new_patient = Patient.objects.create(**payload)
        new_payload = {
            "name": [
                {
                    "family": "My Surname",
                    "given": ["My Name"]
                }
            ],
            "gender": "female",
            "birthDate": "1999-01-01",
            "address": [
                {
                    "city": "City A",
                    "state": "State A",
                    "postalCode": "1234-567"
                }
            ],
            "resourceType": "Patient",
            "telecom": [
                {
                    "system": "email",
                    "value": "me@mail.com"
                }
            ]
        }
        update_status: int = Patient.objects.filter(id=new_patient.id).update(**new_payload)
        new_patient = Patient.objects.get(id=new_patient.id)
        self.assertEqual(update_status, 1)
        self.assertEqual(new_patient.address, [{"city": "City A", "state": "State A", "postalCode": "1234-567"}])
        self.assertEqual(new_patient.birthDate, datetime.date(1999, 1, 1))
        self.assertEqual(new_patient.gender, "female")
        self.assertEqual(new_patient.name, [{"family": "My Surname", "given": ["My Name"]}])
        self.assertEqual(new_patient.resourceType, "Patient")
        self.assertEqual(new_patient.telecom, [{"system": "email", "value": "me@mail.com"}])

    def test_delete_object_using_delete_object_method(self):
        payload = copy.deepcopy(PAYLOAD)
        new_patient = Patient.objects.create(**payload)
        deletion_status = new_patient.delete()[0]
        self.assertEqual(deletion_status, 1)

    def test_delete_object_using_delete_model_method_when_specifying_a_non_existing_id_returns_zero(self):
        is_deleted: int = Patient.objects.filter(id=0).delete()[0]
        self.assertEqual(is_deleted, 0)

    def test_delete_object_using_delete_model_method_when_specifying_an_existing_id_deletes_successfully(self):
        payload = copy.deepcopy(PAYLOAD)
        new_patient = Patient.objects.create(**payload)
        is_deleted: int = Patient.objects.filter(id=new_patient.id).delete()[0]
        self.assertEqual(is_deleted, 1)
