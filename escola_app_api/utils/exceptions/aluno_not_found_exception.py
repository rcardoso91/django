class AlunoNotFoundException(Exception):
    def __init__(self, aluno: str) -> None:
        super().__init__(f"Aluno ({aluno}) not found")
