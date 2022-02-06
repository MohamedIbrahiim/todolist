from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class RegisterTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_dict = {
                "username": "test@username.com",
                "email": "test@mail.com",
                "first_name": "Test",
                "last_name": "end-user",
                "password": "12345678"
            }

    def test_200_ok(self) -> None:
        response = self.client.post(
            reverse("mobile:register"),
            self.user_dict
        )
        user = User.objects.get(username="test@username.com")
        assert response.status_code == 201
        assert User.objects.count() == 1
        assert user.email == "test@mail.com"
