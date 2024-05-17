import json
import jwt
import os
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from escola_app_api.models.aluno_model import aluno
from .factories.aluno_factory import alunoeFactory


class RestApiTestE2e(TestCase):
    client = Client()
    cookies = f"token={jwt.encode({"sub": 1}, os.environ.get("JWT_SECRET"), algorithm="HS256")}"

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_delete_aluno(self) -> None:
        alunoeFactory("Thomas Frank")
        self.client.cookies.load(self.cookies)
        response = self.client.delete("/api/aluno/1")
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(aluno.DoesNotExist):
            aluno.objects.get(codigo_aluno=1)

    def test_delete_unexistest_aluno(self):
        self.client.cookies.load(self.cookies)
        response = self.client.delete("/api/aluno/1")
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "aluno (1) not found")

    def test_delete_without_token(self):
        alunoeFactory("Thomas Frank")
        self.client.cookies.clear()
        response = self.client.delete("/api/aluno/1")
        self.assertEqual(response.status_code, 401)

