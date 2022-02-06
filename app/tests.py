from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from app.models import Todo


class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_dict = {
            "username": "test@username.com",
            "email": "test@mail.com",
            "first_name": "Test",
            "last_name": "end-user",
            "password": "12345678",
        }


class RegisterTest(BaseTest):
    def test_200_ok(self) -> None:
        response = self.client.post(reverse("mobile:register"), self.user_dict)
        user = User.objects.get(username="test@username.com")
        assert response.status_code == 201
        assert User.objects.count() == 1
        assert user.email == "test@mail.com"

    def test_400_wrong_data(self) -> None:
        del self.user_dict["password"]
        response = self.client.post(reverse("mobile:register"), self.user_dict)
        assert response.status_code == 400
        assert User.objects.count() == 0


class ToDoTest(BaseTest):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.admin = User.objects.create_superuser(
            username="admin@test.com", password="12345678"
        )

    def setUp(self) -> None:
        self.client = APIClient()
        self.client.post(reverse("mobile:register"), self.user_dict)
        user = User.objects.get(username="test@username.com")
        self.client.force_authenticate(user)
        self.todo_obj, created = Todo.objects.get_or_create(
            creator=self.admin,
            description="string",
            due_date="2022-02-06T12:22:09.288Z",
            end_user=user,
        )

    def test_list_200_ok(self):
        response = self.client.get(reverse("mobile:todo-list"))
        assert response.status_code == 200

    def test_update_200_ok(self):
        response = self.client.patch(
            reverse("mobile:todo-detail", args=(str(self.todo_obj.id))), {}
        )
        assert response.status_code == 200

    def test_update_404_not_found(self):
        self.todo_obj.is_finished = True
        self.todo_obj.save()
        response = self.client.patch(
            reverse("mobile:todo-detail", args=(str(self.todo_obj.id))), {}
        )
        assert response.status_code == 404
