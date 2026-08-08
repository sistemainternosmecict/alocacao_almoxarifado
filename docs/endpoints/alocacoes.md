🏷️ Endpoints de Alocações (/alocacao)

Abaixo estão detalhadas as rotas implementadas no controller de alocações (routers/controller_alocacao.py):

📚 Documentação da API

Com a aplicação em execução, a documentação OpenAPI gerada pelo FastAPI pode ser acessada em:

    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

```text
Método: POST
Rota: /alocacao
Status code: 201

Headers:
Location header com URI do recurso criado.
Descrição: Cria uma nova alocação associando uma lista de IDs de equipamentos a um contexto/escola, e define quantidade e observações.
Retorna: Alocacao_response
```

```text
Método: GET
Rota: /alocacao
Status code: 200 OK

Descrição: Obtém a lista de todas as alocações cadastradas, decompondo os equipamentos associados para apresentar suas especificações e dados reais ao invés de apenas IDs.
Retorna: List_alocacao_response
```

```text
Método: GET
Rota: /alocacao/{alocacao_id}
Status code: 200 OK

Descrição: Busca os dados de uma alocação específica pelo seu ID, populando os objetos de equipamento relacionados a ela.
Retorna: Alocacao_response
```

```text
Método: PUT
Rota: /alocacao/{alocacao_id}
Status code: 200 OK

Descrição: Atualiza o status da alocação (ex: Em vigor, Encerrada).
Retorna: Atualizar_alocacao_response
```
