from django.urls import path
from .views.rest_views import restAlunoView, restAlunoCodeView, sessionView
from .views.template_views import (
    templateAlunoListView,
    templateAlunoCreateView,
    templateAlunoEditView,
)

urlpatterns = [
    # REST API
    path("session/", sessionView),
    path("aluno/", restAlunoView),
    path('aluno/<int:codigo_aluno>', restAlunoCodeView),

    # Template API
    path("aluno/app/home", templateAlunoListView, name='aluno_list'),
    path("aluno/app/create", templateAlunoCreateView, name='aluno_create'),
    path("aluno/app/edit/<int:codigo_aluno>", templateAlunoEditView, name='aluno_edit'),
]
