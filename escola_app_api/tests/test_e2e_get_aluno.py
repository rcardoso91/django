import json
import jwt
import os
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from .factories.aluno_factory import alunoeFactory


class RestApiTestE2e(TestCase):
    client = Client()
    cookies = f"token={jwt.encode({"sub": 1}, os.environ.get("JWT_SECRET"), algorithm="HS256")}"


    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_get_aluno(self) -> None:
        name = "John Doe"
        alunoeFactory(name)
        self.client.cookies.load(self.cookies)
        response = self.client.get("/api/aluno/1")
        responseBody = json.loads(response.content.decode("utf-8"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseBody["aluno"]["name"], name)

    def test_get_unexistent_aluno(self) -> None:
        self.client.cookies.load(self.cookies)
        response = self.client.get("/api/aluno/1")
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "aluno (1) not found")

    def test_get_aluno_without_token(self) -> None:
        name = "John Doe"
        alunoeFactory(name)
        self.client.cookies.clear()
        response = self.client.get("/api/aluno/1")
        self.assertEqual(response.status_code, 401)
        
