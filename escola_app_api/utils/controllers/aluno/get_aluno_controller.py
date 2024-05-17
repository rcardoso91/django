from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK
from ....models.aluno_model import Aluno
from ...assertions.assert_alunos_exists import assertAlunoExists
from ...decorators.rest_auth_required_decorator import restAuthRequired


@restAuthRequired
def obterAlunoController(request: Request, codigo_aluno: int) -> Response:
    aluno = Aluno.buscar_por_codigo(codigo_aluno)
    assertAlunoExists(aluno, codigo_aluno)
    return Response({"aluno": aluno.apresentar()}, status=HTTP_200_OK)
