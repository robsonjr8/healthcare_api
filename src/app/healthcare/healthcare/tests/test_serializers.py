import copy

from django.test import TestCase
from rest_framework.serializers import ErrorDetail

from app.healthcare.healthcare.api.serializers import PatientSerializer
from app.healthcare.healthcare.tests.test_setup import PAYLOAD


class TestPatientSerializer(TestCase):
    """See examples here: https://www.hl7.org/fhir/patient-examples.html"""
    def test_when_providing_none_value_returns_false(self):
        serializer: PatientSerializer = PatientSerializer(data=None)
        self.assertFalse(serializer.is_valid())

    def test_when_name_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["name"] = "Patient Name"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_birthdate_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["birthDate"] = "0000-00-00"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_address_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["address"] = "My Address"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_telecom_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["telecom"] = "My contact"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_name_key_is_missing_in_provided_data_returns_false_and_error_details(self):
        payload = copy.deepcopy(PAYLOAD)
        payload.pop("name")
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {'name': [ErrorDetail(string='This field is required.', code='required')]})

    def test_when_birthdate_key_is_missing_in_provided_data_returns_false_and_error_details(self):
        payload = copy.deepcopy(PAYLOAD)
        payload.pop("birthDate")
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {'birthDate': [ErrorDetail(string='This field is required.', code='required')]})

    def test_when_address_key_is_missing_in_provided_data_returns_false_and_error_details(self):
        payload = copy.deepcopy(PAYLOAD)
        payload.pop("address")
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {'address': [ErrorDetail(string='This field is required.', code='required')]})

    def test_when_telecom_key_is_missing_in_provided_data_returns_false_and_error_details(self):
        payload = copy.deepcopy(PAYLOAD)
        payload.pop("telecom")
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {'telecom': [ErrorDetail(string='This field is required.', code='required')]})

    def test_when_resource_type_key_is_missing_in_provided_data_returns_false_and_error_details(self):
        payload = copy.deepcopy(PAYLOAD)
        payload.pop("resourceType")
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors, {'resourceType': [ErrorDetail(string='This field is required.', code='required')]})

    def test_when_active_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["active"] = "active"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_active_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["active"] = True
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_deceasedBoolean_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["deceasedBoolean"] = "deceasedBoolean"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_deceasedBoolean_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["deceasedBoolean"] = True
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_maritalStatus_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["maritalStatus"] = "maritalStatus"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_maritalStatus_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["maritalStatus"] = {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "36629006",
                    "display": "Legally married"
                },
                {
                    "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
                    "code": "M"
                }
            ]
        }
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_multipleBirthInteger_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["multipleBirthInteger"] = "multipleBirthInteger"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_multipleBirthInteger_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["multipleBirthInteger"] = 2
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_photo_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["photo"] = "photo"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_photo_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["photo"] = [
            {
                "contentType": "image/png",
                "data": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
            }
        ]
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_contact_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["contact"] = "contact"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_contact_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["contact"] = [
            {
                "relationship": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0131",
                                "code": "N"
                            }
                        ]
                    }
                ],
                "name": {
                    "family": "du Marché",
                    "_family": {
                        "extension": [
                            {
                                "url": "http://hl7.org/fhir/StructureDefinition/humanname-own-prefix",
                                "valueString": "VV"
                            }
                        ]
                    },
                    "given": ["Bénédicte"]
                },
                "telecom": [
                    {
                        "system": "phone",
                        "value": "+33 (237) 998327"
                    }
                ],
                "address": {
                    "use": "home",
                    "type": "both",
                    "line": ["534 Erewhon St"],
                    "city": "PleasantVille",
                    "district": "Rainbow",
                    "state": "Vic",
                    "postalCode": "3999",
                    "period": {
                        "start": "1974-12-25"
                    }
                },
                "gender": "female",
                "period": {
                    "start": "2012"
                }
            }
        ]
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_communication_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["communication"] = "communication"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_communication_key_in_provided_data_is_valid_returns_true(self):
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
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_generalPractitioner_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["generalPractitioner"] = "generalPractitioner"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_generalPractitioner_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["generalPractitioner"] = [
            {
                "reference": "Practitioner/example",
                "display": "Dr Adam Careful"
            }
        ]
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_managingOrganization_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["managingOrganization"] = "managingOrganization"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_managingOrganization_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["managingOrganization"] = {
            "reference": "Organization",
            "display": "Healthcare Inc"
        }
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_link_key_in_provided_data_is_not_valid_returns_false(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["link"] = "link"
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertFalse(serializer.is_valid())

    def test_when_link_key_in_provided_data_is_valid_returns_true(self):
        payload = copy.deepcopy(PAYLOAD)
        payload["link"] = [
            {
                "other": {
                    "reference": "Patient/pat2"
                },
                "type": "seealso"
            }
        ]
        serializer: PatientSerializer = PatientSerializer(data=payload)
        self.assertTrue(serializer.is_valid())

    def test_when_provided_data_is_valid_returns_true(self):
        serializer: PatientSerializer = PatientSerializer(data=PAYLOAD)
        self.assertTrue(serializer.is_valid())
