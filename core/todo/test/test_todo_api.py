import pytest
from rest_framework.test import APIClient

from accounts.models import User
from ..models import Task


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(username="admin", password="123")
    return user


@pytest.fixture
def task(common_user):
    task = Task.objects.create(user=common_user, title="test", completed=True)
    return task


@pytest.mark.django_db
class TestTodoAPi:

    # for get task
    def test_get_task_response_200_status(self, api_client, common_user):
        api_client.force_authenticate(common_user)
        
        url = "http://127.0.0.1:8000/api/v1/task/"
        response = api_client.get(url)

        assert response.status_code == 200

    # get single task
    def test_get_single_task_200_status(self, api_client, task, common_user):
        api_client.force_authenticate(common_user)

        url = "http://127.0.0.1:8000/api/v1/task/"  
        response = api_client.get(url, kwargs={"pk": task.id})

        assert response.status_code == 200

    # for create task without login
    def test_create_task_without_login(self, api_client):
        url = "http://127.0.0.1:8000/api/v1/task/"
        data = {"title": "test", "completed": True}
        response = api_client.post(url, data)

        assert response.status_code == 403

    # for create task with login
    def test_create_task_with_login(self, api_client, common_user):
        url = "http://127.0.0.1:8000/api/v1/task/"
        data = {"title": "test", "completed": True}
        api_client.force_authenticate(common_user)
        response = api_client.post(url, data)

        assert response.status_code == 201

    # delete task without login
    def test_delete_task_without_login(self, api_client, task):
        url = f"http://127.0.0.1:8000/api/v1/task/{task.id}/"
        response = api_client.delete(url, kwargs={"pk": task.id})

        assert response.status_code == 403

    # delete task with login
    def test_delete_task_with_login(self, api_client, common_user, task):
        url = f"http://127.0.0.1:8000/api/v1/task/{task.id}/"
        api_client.force_authenticate(common_user)
        response = api_client.delete(url, kwargs={"pk": task.id})

        assert response.status_code == 204

    # update a task without login
    def test_update_task_without_login(self, api_client, task):
        url = f"http://127.0.0.1:8000/api/v1/task/{task.id}/"
        data = {"title": "update_test", "compelted": False}
        response = api_client.put(url, data)

        assert response.status_code == 403

    # update a task with login
    def test_update_task_with_login(self, api_client, common_user, task):
        url = f"http://127.0.0.1:8000/api/v1/task/{task.id}/"
        data = {"title": "update_test", "compelted": False}
        api_client.force_authenticate(common_user)
        response = api_client.put(url, data)

        assert response.status_code == 200
        assert response.data["title"] == "update_test"
        assert response.data["completed"] is False
