
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from ..utils.controllers.aluno.create_aluno_controller import (
    createAlunoController,
)
from ..utils.controllers.aluno.list_alunos_controller import listarAlunosController
from ..utils.controllers.aluno.get_aluno_controller import obterAlunoController
from ..utils.controllers.aluno.update_aluno_controller import (
    atualizarAlunoController,
)
from ..utils.controllers.aluno.delete_aluno_controller import (
    deleteAlunoController,
)
from ..utils.controllers.session.create_session_controller import (
    createSessionController,
)
from ..utils.controllers.session.delete_session_controller import (
    deleteSessionController,
)
from ..utils.decorators.rest_error_handler_decorator import restErrorHandler


import logging
from logging.handlers import RotatingFileHandler
from django.conf import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = RotatingFileHandler(settings.LOG_FILE_PATH, maxBytes=1024*1024*10, backupCount=5)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)





@api_view(["POST", "DELETE"])
@restErrorHandler
def sessionView(request: Request) -> Response:
    logger.info("Chamando sessionView")
    controllers = {"POST": createSessionController, "DELETE": deleteSessionController}
    return controllers[request.method](request)



import logging
logger = logging.getLogger(__name__)

@api_view(["GET", "PUT", "DELETE"])
@restErrorHandler
def restAlunoCodeView(request: Request, codigo_aluno: int) -> Response:
    logger.info(f"Chamando restAlunoCodeView - Método HTTP: {request.method}")

    controllers = {
        "GET": obterAlunoController,
        "PUT": atualizarAlunoController,
        "DELETE": deleteAlunoController,
    }
    return controllers[request.method](request, codigo_aluno=codigo_aluno)




@api_view(["POST", "GET"])
@restErrorHandler
def restAlunoView(request: Request) -> Response:
    controllers = {
        "POST": createAlunoController,
        "GET": listarAlunosController,
    }
    return controllers[request.method](request)



