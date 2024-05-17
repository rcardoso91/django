from typing import Optional, List, Any
from django.db import models
from datetime import date
import logging

class Aluno(models.Model):
    codigo_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, null=False)
    data_nascimento = models.DateField(null=False)
    criado_em = models.DateField(auto_now=True)
    endereco_rua = models.CharField(max_length=80, null=False)
    endereco_numero = models.IntegerField(null=False)

    @staticmethod
    def buscar_por_codigo(codigo_aluno: int) -> Optional["Aluno"]:
        try:
            aluno = Aluno.objects.get(codigo_aluno=codigo_aluno)
            return aluno
        except Aluno.DoesNotExist:
            return None

    @staticmethod
    def buscar_muitos(**kwargs: Any) -> List["Aluno"]:
        alunos = Aluno.objects.all().order_by("-criado_em")
        if kwargs:
            kwargs_conteudo = {
                f"{chave}__icontains": valor for chave, valor in kwargs.items()
            }
            return alunos.filter(**kwargs_conteudo)
        return alunos

    @staticmethod
    def criar(nome: str, data_nascimento: date, endereco_rua: str, endereco_numero: int) -> int:
        try:
            aluno = Aluno.objects.create(
                nome=nome,
                data_nascimento=data_nascimento,
                endereco_rua=endereco_rua,
                endereco_numero=endereco_numero,
            )
            logging.info(f"Aluno criado com sucesso: {aluno.nome}")
            return aluno.codigo_aluno
        except Exception as e:
            logging.error(f"Erro ao criar aluno: {e}")
            raise

    def apresentar(self) -> dict:
        return {
            "codigo_aluno": self.codigo_aluno,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "criado_em": self.criado_em,
            "endereco_rua": self.endereco_rua,
            "endereco_numero": self.endereco_numero,
        }

    def __str__(self) -> str:
        return f"({self.codigo_aluno}) {self.nome}"
