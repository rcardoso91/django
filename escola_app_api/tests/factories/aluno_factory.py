from faker import Faker
from typing import Optional
from escola_app_api.models.aluno_model import aluno


def alunoeFactory(
    name: Optional[str] = None,
) -> aluno:
    faker = Faker()
    name = faker.name() if name is None else name
    aluno = aluno.objects.create(
        name=name,
        data_nascimento=faker.data_nascimento(minimum_age=15, maximum_age=50),
        endereco_rua=faker.street_address(),
        endereco_numero=faker.random_int(min=1, max=1000),
    )
    return aluno
