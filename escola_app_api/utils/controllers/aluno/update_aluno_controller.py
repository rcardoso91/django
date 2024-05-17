from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from ....models.aluno_model import Aluno
from ...assertions.assert_alunos_exists import assertAlunoExists
from ...decorators.rest_auth_required_decorator import restAuthRequired
from ...assertions.assert_authentication_and_get_user_id import (
    assertAuthenticationAndGetUserId,
)
from ...serializers.update_aluno_request_serializer import (
    UpdateAlunoRequestSerializer,
)
from ...assertions.assert_request_payload_is_valid_and_get_serialized_data import (
    assertRequestPayloadIsValidAndGetSerializedData,
)

def atualizarAlunoController(request, codigo_aluno):
    try:
        aluno = Aluno.objects.get(codigo_aluno=codigo_aluno)
    except Aluno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    data = request.data
    aluno.nome = data.get("nome", aluno.nome)
    aluno.data_nascimento = data.get("data_nascimento", aluno.data_nascimento)
    aluno.endereco_rua = data.get("endereco_rua", aluno.endereco_rua)
    aluno.endereco_numero = data.get("endereco_numero", aluno.endereco_numero)
    
    aluno.save()
    return Response(aluno.apresentar(), status=status.HTTP_200_OK)
