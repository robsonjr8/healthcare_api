import copy

from rest_framework import status
from rest_framework.serializers import ErrorDetail
from rest_framework.test import force_authenticate

from app.healthcare.healthcare.tests.test_setup import TestSetUp, PAYLOAD


class TestCreatePatientNew(TestSetUp):
    def test_create_patient_when_not_authenticated_the_requester_is_not_able_to_create_a_new_record(self):
        payload = copy.deepcopy(PAYLOAD)
        request = self.factory.post('/fhir/Patient/', data=payload, format="json")
        response = self.create_view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_patient_when_authenticated_but_without_a_payload_the_requester_is_not_able_to_create_a_new_record(self):
        request = self.factory.post('/fhir/Patient/')
        force_authenticate(request, user=self.user)
        response = self.create_view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_patient_when_authenticated_but_providing_an_invalid_payload_the_requester_is_not_able_to_create_a_new_record(self):
        request = self.factory.post('/fhir/Patient/', data={"invalid": "payload"}, format="json")
        force_authenticate(request, user=self.user)
        response = self.create_view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_patient_when_authenticated_and_providing_a_valid_payload_it_creates_a_new_record_successfully(self):
        payload = copy.deepcopy(PAYLOAD)
        request = self.factory.post('/fhir/Patient/', data=payload, format="json")
        force_authenticate(request, user=self.user)
        response = self.create_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["address"], [{'city': 'My City', 'state': 'My State', 'postalCode': '1234-000'}])
        self.assertEqual(response.data["birthDate"], "2000-01-01")
        self.assertEqual(response.data["gender"], "male")
        self.assertEqual(response.data["name"], [{'family': 'Surname', 'given': ['First Name']}])
        self.assertEqual(response.data["resourceType"], "Patient")
        self.assertEqual(response.data["telecom"], [{'system': 'email', 'value': 'patient@mail.com'}])


class TestDeletePatient(TestSetUp):
    def test_delete_patient_when_specifying_a_non_existing_patient_id_returns_404(self):
        request = self.factory.delete('/fhir/Patient')
        force_authenticate(request, user=self.user)
        response = self.delete_view(request, pk=0)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'detail': ErrorDetail(string='No Patient matches the given query.', code='not_found')})

    def test_delete_patient_when_specifying_an_existing_patient_id_returns_204(self):
        payload = copy.deepcopy(PAYLOAD)
        req = self.factory.post('/fhir/Patient/', data=payload, format="json")
        force_authenticate(req, user=self.user)
        res = self.create_view(req)
        request = self.factory.delete('/fhir/Patient')
        force_authenticate(request, user=self.user)
        response = self.delete_view(request, pk=res.data["id"])
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestRetrievePatientList(TestSetUp):
    def test_retrieve_all_patients_records_when_requester_is_not_authenticated_returns_401(self):
        request = self.factory.get('/fhir/Patient')
        response = self.list_view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_all_patients_records_when_requester_is_authenticated_returns_200(self):
        request = self.factory.get('/fhir/Patient')
        force_authenticate(request, user=self.user)
        response = self.list_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)


class TestRetrievePatient(TestSetUp):
    def test_retrieve_patient_record_when_requester_is_not_authenticated_returns_401(self):
        request = self.factory.get('/fhir/Patient')
        response = self.retrieve_view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_patient_record_when_specifying_a_non_existing_patient_id_returns_404(self):
        request = self.factory.get('/fhir/Patient')
        force_authenticate(request, user=self.user)
        response = self.retrieve_view(request, pk=0)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'detail': ErrorDetail(string='No Patient matches the given query.', code='not_found')})

    def test_retrieve_patient_record_when_specifying_an_existing_patient_id_returns_200(self):
        payload = copy.deepcopy(PAYLOAD)
        req = self.factory.post('/fhir/Patient/', data=payload, format="json")
        force_authenticate(req, user=self.user)
        res = self.create_view(req)
        request = self.factory.get('/fhir/Patient')
        force_authenticate(request, user=self.user)
        response = self.retrieve_view(request, pk=res.data["id"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["address"], res.data["address"])
        self.assertEqual(response.data["birthDate"], res.data["birthDate"])
        self.assertEqual(response.data["gender"], res.data["gender"])
        self.assertEqual(response.data["name"], res.data["name"])
        self.assertEqual(response.data["resourceType"], res.data["resourceType"])
        self.assertEqual(response.data["telecom"], res.data["telecom"])


class TestPartialUpdatePatient(TestSetUp):
    def test_partial_update_patient_record_when_specifying_a_non_existing_patient_id_returns_404(self):
        request = self.factory.patch('/fhir/Patient')
        force_authenticate(request, user=self.user)
        response = self.partial_update_view(request, pk=0)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'detail': ErrorDetail(string='No Patient matches the given query.', code='not_found')})

    def test_partial_update_patient_record_when_specifying_an_existing_patient_id_returns_200(self):
        payload = copy.deepcopy(PAYLOAD)
        req = self.factory.post('/fhir/Patient/', data=payload, format="json")
        force_authenticate(req, user=self.user)
        res = self.create_view(req)
        request = self.factory.patch('/fhir/Patient', data={"birthDate": "2000-12-31"}, format="json")
        force_authenticate(request, user=self.user)
        response = self.partial_update_view(request, pk=res.data["id"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["address"], res.data["address"])
        self.assertEqual(response.data["birthDate"], "2000-12-31")
        self.assertEqual(response.data["gender"], res.data["gender"])
        self.assertEqual(response.data["name"], res.data["name"])
        self.assertEqual(response.data["resourceType"], res.data["resourceType"])
        self.assertEqual(response.data["telecom"], res.data["telecom"])


class TestUpdatePatient(TestSetUp):
    def test_update_patient_record_when_specifying_a_non_existing_patient_id_returns_404(self):
        request = self.factory.put('/fhir/Patient')
        force_authenticate(request, user=self.user)
        response = self.update_view(request, pk=0)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'detail': ErrorDetail(string='No Patient matches the given query.', code='not_found')})

    def test_update_patient_record_when_specifying_an_existing_patient_id_returns_200(self):
        payload = copy.deepcopy(PAYLOAD)
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
        req = self.factory.post('/fhir/Patient/', data=payload, format="json")
        force_authenticate(req, user=self.user)
        res = self.create_view(req)
        request = self.factory.put('/fhir/Patient', data=new_payload, format="json")
        force_authenticate(request, user=self.user)
        response = self.update_view(request, pk=res.data["id"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["address"], [{"city": "City A", "state": "State A", "postalCode": "1234-567"}])
        self.assertEqual(response.data["birthDate"], "1999-01-01")
        self.assertEqual(response.data["gender"], "female")
        self.assertEqual(response.data["name"], [{"family": "My Surname", "given": ["My Name"]}])
        self.assertEqual(response.data["resourceType"], "Patient")
        self.assertEqual(response.data["telecom"], [{"system": "email", "value": "me@mail.com"}])
