🏷️ Endpoints de Categorias (/categoria)

Abaixo estão detalhadas as rotas implementadas no controller de categorias de equipamentos (routers/categoria_controller.py):

📚 Documentação da API

Com a aplicação em execução, a documentação OpenAPI gerada pelo FastAPI pode ser acessada em:

    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc

```text
Método: POST
Rota: /categoria
Status code: 201

Headers:
Created	Cria uma nova categoria de equipamento
Location header com URI do recurso criado.
Retorna Categoria_equipamento_response
```

```text
Método: GET
Rota: /categoria
Status code: 200 OK

Headers:
Obtém a lista de todas as categorias cadastradas
Retorna List_categoria_equipamento_response
```

```text
Método: GET
Rota: /categoria/{categoria_id}
Status code: 200 OK

Headers:
Busca os dados de uma categoria específica pelo seu ID
Retorna Categoria_equipamento_response
```

```text
Método: DELETE
Rota: /categoria/{categoria_id}
Status code: 204

Headers:
Remove uma categoria de equipamento pelo seu ID	Sem corpo de resposta (Response vazio)
Retorna No Content
```
