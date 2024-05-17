from typing import Optional
from ...models.aluno_model import Aluno
from ..exceptions.aluno_not_found_exception import AlunoNotFoundException


def assertAlunoExists(aluno: Optional[Aluno], aluno_identifier: str) -> None:
    if not isinstance(aluno, Aluno):
        raise AlunoNotFoundException(aluno_identifier)
