
## Modelo de dados

```sql
CREATE TABLE Aluno (
    CODIGO_ALUNO INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(80) NOT NULL,
    data_nascimento DATE NOT NULL,
    criado_em DATE DEFAULT CURRENT_TIMESTAMP,
    endereco_rua VARCHAR(80) NOT NULL,
    endereco_numero INT NOT NULL
);
```

## Teste a aplicação em sua máquina

Certifique-se de ter o Docker instalado em sua máquina antes de prosseguir.

- [Docker](https://www.docker.com/)

1. Faça o clone do projeto

```bash
git clone https://github.com/rcardoso91/django.git
```

2. Navegue até diretório do projeto e execute os containers docker com o comando:

```bash
docker compose up -d --build
```

3. Verifique se os containers foram executados com sucesso com o comando:

```bash
docker compose logs
```

4. Com os conatiners em execução, você pode:

- Testar a API REST (Uma breve documentação das rotas se encontra no arquivo `api.http`).
- Acessar a aplicação pela rota:

```bash
http://localhost:8000/api/aluno/app/home
```

## Credenciais

- email: admin@teste.com.br
- password: admin
