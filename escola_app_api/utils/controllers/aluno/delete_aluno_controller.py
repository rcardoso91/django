from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from ....models.aluno_model import Aluno
from ...decorators.rest_auth_required_decorator import restAuthRequired
from ...assertions.assert_alunos_exists import assertAlunoExists

import logging
logger = logging.getLogger(__name__)

@restAuthRequired
def deleteAlunoController(request: Request, codigo_aluno: int) -> Response:
    try:
        logger.info(f"Recebida requisição DELETE para aluno com código {codigo_aluno}")
        
        # Log para verificar se o request foi autenticado corretamente
        logger.info(f"Usuário autenticado: {request.user}")
        
        aluno = Aluno.buscar_por_codigo(codigo_aluno)
        
        if aluno is None:
            logger.warning(f"Aluno com código {codigo_aluno} não encontrado")
            return Response({"detail": "Aluno não encontrado"}, status=HTTP_404_NOT_FOUND)
        
        logger.info(f"Aluno encontrado: {aluno}")
        aluno.delete()
        logger.info(f"Aluno com código {codigo_aluno} deletado com sucesso") 
        return Response(status=HTTP_204_NO_CONTENT)
    
    except Exception as e:
        logger.error(f"Erro ao deletar aluno com código {codigo_aluno}: {e}", exc_info=True)
        return Response({"detail": "Erro interno do servidor"}, status=HTTP_500_INTERNAL_SERVER_ERROR)
