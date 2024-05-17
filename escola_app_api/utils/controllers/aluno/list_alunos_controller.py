import logging
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from ....models.aluno_model import Aluno
from ...decorators.rest_auth_required_decorator import restAuthRequired

# Configurar o logger
logger = logging.getLogger(__name__)


    
@restAuthRequired
def listarAlunosController(request: Request) -> Response:
    try:
        nomeFiltro = request.query_params.get("nome", "")
        enderecoFiltro = request.query_params.get("endereco_rua", "")
        codigoAlunoFiltro = request.query_params.get("codigo_aluno", "")
        numeroEnderecoFiltro = request.query_params.get("endereco_numero", "")

        alunos = Aluno.buscar_muitos(
            nome=nomeFiltro,
            endereco_rua=enderecoFiltro,
            codigo_aluno=codigoAlunoFiltro,
            endereco_numero=numeroEnderecoFiltro,
        )

        alunosApresentacao = [aluno.apresentar() for aluno in alunos]
        return Response({"alunos": alunosApresentacao}, status=HTTP_200_OK)
    except Exception as e:
        logger.error(f"Erro ao listar alunos: {e}", exc_info=True)
        return Response({"error": "Erro interno no servidor"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
