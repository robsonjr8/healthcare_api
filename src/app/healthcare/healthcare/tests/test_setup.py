from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIRequestFactory

from app.healthcare.healthcare.api.utils.types import FHIRdata
from app.healthcare.healthcare.api.views import PatientViewSet


PAYLOAD: FHIRdata = {
    "name": [
        {
            "family": "Surname",
            "given": ["First Name"]
        }
    ],
    "gender": "male",
    "birthDate": "2000-01-01",
    "address": [
        {
            "city": "My City",
            "state": "My State",
            "postalCode": "1234-000"
        }
    ],
    "resourceType": "Patient",
    "telecom": [
        {
            "system": "email",
            "value": "patient@mail.com"
        }
    ]
}


class TestSetUp(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user: User = User.objects.create_user(
            username="my_user",
            email="user@mail.com",
            password="my_password"
        )
        self.create_view = PatientViewSet.as_view(actions={"post": "create"})
        self.delete_view = PatientViewSet.as_view(actions={"delete": "destroy"})
        self.list_view = PatientViewSet.as_view(actions={"get": "list"})
        self.retrieve_view = PatientViewSet.as_view(actions={"get": "retrieve"})
        self.partial_update_view = PatientViewSet.as_view(actions={"patch": "partial_update"})
        self.update_view = PatientViewSet.as_view(actions={"put": "update"})
        return super().setUp()

    def tearDown(self):
        self.client.logout()
        return super().tearDown()
