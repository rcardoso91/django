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

    def test_update_aluno(self) -> None:
        aluno = alunoeFactory("Thomas Frank")
        data = {
            "name": "John Doe",
            "data_nascimento": str(aluno.data_nascimento),
            "endereco_rua": aluno.endereco_rua,
            "endereco_numero": aluno.endereco_numero,
        }
        data_json = json.dumps(data)
        self.client.cookies.load(self.cookies)
        response = self.client.put(
            "/api/aluno/1", data=data_json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 204)
        alunoOnDatabase = aluno.objects.get(codigo_aluno=1)
        self.assertEqual(alunoOnDatabase.name, data["name"])

    def test_update_aluno_with_invalid_payload(self):
        alunoeFactory(name="Thomas Frank")
        data = {
            "name": "John Doe",
            "data_nascimento": "1990-05-15",
            "endereco_rua": "Pine Street West",
        }
        data_json = json.dumps(data)
        self.client.cookies.load(self.cookies)
        response = self.client.put(
            "/api/aluno/1", data=data_json, content_type="application/json"
        )
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data["message"], "Invalid request payload")

    def test_update_unexistest_aluno(self):
        data = {
            "name": "John Doe",
            "data_nascimento": "1990-05-15",
            "endereco_rua": "Pine Street West",
            "endereco_numero": 45,
        }
        data_json = json.dumps(data)
        self.client.cookies.load(self.cookies)
        response = self.client.put(
            "/api/aluno/1", data=data_json, content_type="application/json"
        )
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "aluno (1) not found")


    def test_update_aluno_without_token(self) -> None:
        aluno = alunoeFactory("Thomas Frank")
        data = {
            "name": "John Doe",
            "data_nascimento": str(aluno.data_nascimento),
            "endereco_rua": aluno.endereco_rua,
            "endereco_numero": aluno.endereco_numero,
        }
        data_json = json.dumps(data)
        self.client.cookies.clear()
        response = self.client.put(
            "/api/aluno/1", data=data_json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)
