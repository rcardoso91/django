import json
from django.template import loader
from django.http import HttpResponse, HttpRequest
from ..models.aluno_model import Aluno
from ..utils.decorators.template_auth_required_decorator import templateAuthRequired
import logging

logger = logging.getLogger(__name__)

@templateAuthRequired
def templateAlunoListView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("aluno-list.html")
    alunos = Aluno.buscar_muitos()
    context = {"alunos": alunos}
    return HttpResponse(template.render(context, request))

@templateAuthRequired
def templateAlunoCreateView(request: HttpRequest) -> HttpResponse:
    try:
        template = loader.get_template("aluno-create.html")
        return HttpResponse(template.render(None, request))
    except Exception as e:
        logger.error(f"Erro ao renderizar template de criação de aluno: {e}")
        return HttpResponse(status=500)

@templateAuthRequired
def templateAlunoEditView(request: HttpRequest, codigo_aluno: int) -> HttpResponse:
    aluno = Aluno.buscar_por_codigo(codigo_aluno)
    if aluno is None:
        template = loader.get_template("aluno-404.html")
        return HttpResponse(template.render(None, request))
    template = loader.get_template("aluno-edit.html")
    context = {"aluno": aluno}
    return HttpResponse(template.render(context, request))
