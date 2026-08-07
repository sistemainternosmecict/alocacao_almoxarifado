🏷️ Endpoints de Equipamentos (/equipamento)

Abaixo estão detalhadas as rotas implementadas no controller de equipamentos (routers/controller_equipamento.py):

📚 Documentação da API

Com a aplicação em execução, a documentação OpenAPI gerada pelo FastAPI pode ser acessada em:

    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

```text
Método: POST
Rota: /equipamento
Status code: 201

Headers:
Location header com URI do recurso criado.
Descrição: Cria um novo equipamento vinculando a uma categoria.
Retorna: Equipamento_response
```

```text
Método: GET
Rota: /equipamento
Status code: 200 OK

Descrição: Obtém a lista de todos os equipamentos cadastrados no almoxarifado, trazendo seus detalhamentos de categoria e histórico.
Retorna: List_equipamento_response
```

```text
Método: GET
Rota: /equipamento/{equipamento_id}
Status code: 200 OK

Descrição: Busca os dados de um equipamento específico pelo seu ID, populando sua categoria e histórico.
Retorna: Equipamento_response
```

```text
Método: PUT
Rota: /equipamento/{equipamento_id}
Status code: 200 OK

Descrição: Atualiza o status de um equipamento (novo, defeituoso, manutenção, etc).
Retorna: Atualizar_equipamento_response
```
