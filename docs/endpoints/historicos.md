🏷️ Endpoints de Historicos (/historico)

Abaixo estão detalhadas as rotas implementadas no controller de históricos de equipamentos (routers/controller_historico.py):

📚 Documentação da API

Com a aplicação em execução, a documentação OpenAPI gerada pelo FastAPI pode ser acessada em:

    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

```text
Método: POST
Rota: /historico
Status code: 201

Headers:
Created	Cria um novo histórico de equipamento
Location header com URI do recurso criado.
Retorna Historico_equipamento_response
```

```text
Método: GET
Rota: /historico/{equipamento_id}
Status code: 200 OK

Headers:
Obtém a lista de todos os historicos cadastrados para um equipamento com base no id de equipamento
Retorna List_historico_equipamento_response
```
