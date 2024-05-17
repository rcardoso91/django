from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_201_CREATED
from ....models.aluno_model import Aluno
from ...decorators.rest_auth_required_decorator import restAuthRequired
from ...serializers.create_aluno_request_serialiazer import (
    CreateAlunoRequestSerialiazer,
)
from ...assertions.assert_request_payload_is_valid_and_get_serialized_data import (
    assertRequestPayloadIsValidAndGetSerializedData,
)


@restAuthRequired
def createAlunoController(request: Request) -> Response:
    requestPayload = assertRequestPayloadIsValidAndGetSerializedData(
        request.data, CreateAlunoRequestSerialiazer
    )
    codigo_aluno = Aluno.criar(
        nome=requestPayload.get("nome"),
        data_nascimento=requestPayload.get("data_nascimento"),
        endereco_rua=requestPayload.get("endereco_rua"),
        endereco_numero=requestPayload.get("endereco_numero"),
    )
    return Response(
        {"codigo_aluno": codigo_aluno},
        status=HTTP_201_CREATED,
    )
