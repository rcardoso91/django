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

    def test_list_alunos(self) -> None:
        for _ in range(15):
            alunoeFactory()
        self.client.cookies.load(self.cookies)
        response = self.client.get("/api/aluno/")
        responseBody = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(responseBody["alunos"]), 15)

    def test_list_alunos_without_token(self) -> None:
        for _ in range(15):
            alunoeFactory()
        self.client.cookies.clear()
        response = self.client.get("/api/aluno/")
        self.assertEqual(response.status_code, 401)

