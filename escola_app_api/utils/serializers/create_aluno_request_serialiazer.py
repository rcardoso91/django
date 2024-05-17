from rest_framework import serializers
from ...models.aluno_model import Aluno


class CreateAlunoRequestSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            "nome",
            "data_nascimento",
            "endereco_rua",
            "endereco_numero",
        ]