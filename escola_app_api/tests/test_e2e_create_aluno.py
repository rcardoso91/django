import json
import jwt
import os
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from escola_app_api.models.aluno_model import aluno


class RestApiTestE2e(TestCase):
    client = Client()
    cookies = f"token={jwt.encode({"sub": 1}, os.environ.get("JWT_SECRET"), algorithm="HS256")}"

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_create_aluno(self) -> None:
        data = {
            "name": "John Doe",
            "data_nascimento": "1990-05-15",
            "endereco_rua": "Pine Street West",
            "endereco_numero": 45,
        }
        data_json = json.dumps(data)
        self.client.cookies.load(self.cookies)
        response = self.client.post(
            "/api/aluno/", data=data_json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        alunoOnDatabase = aluno.objects.first()
        self.assertEqual(alunoOnDatabase.name, data["name"])

    def test_create_aluno_with_invalid_payload(self):
        data = {
            "name": "John Doe",
            "data_nascimento": "1990-05-15",
            "endereco_rua": "Pine Street West",
        }
        data_json = json.dumps(data)
        self.client.cookies.load(self.cookies)
        response = self.client.post(
            "/api/aluno/", data=data_json, content_type="application/json"
        )
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data["message"], "Invalid request payload")

    def test_create_aluno_without_token(self):
        data = {
             "name": "John Doe",
            "data_nascimento": "1990-05-15",
            "endereco_rua": "Pine Street West",
            "endereco_numero": 45,
        }
        data_json = json.dumps(data)
        self.client.cookies.clear()
        response = self.client.post(
            "/api/aluno/", data=data_json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)
