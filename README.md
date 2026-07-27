# 📦 API de Alocação de Equipamentos e Controle de Estoque (Secretaria de Educação)

API RESTful desenvolvida para o gerenciamento interno do almoxarifado e acompanhamento de alocações de equipamentos nas unidades escolares e administrativas da **Secretaria de Educação**.

---

## 📋 Sumário

- [Visão Geral](#-visão-geral)
- [Funcionalidades e Casos de Uso](#-funcionalidades-e-casos-de-uso)
- [Arquitetura e Estrutura de Pastas](#-arquitetura-e-estrutura-de-pastas)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Variáveis de Ambiente](#-variáveis-de-ambiente)
- [Instalação e Execução](#-instalação-e-execução)
- [Execução de Testes](#-execução-de-testes)
- [Documentação da API](#-documentação-da-api)

---

## 🎯 Visão Geral

O sistema permite centralizar e automatizar o controle físico do estoque do almoxarifado, bem como todo o ciclo de vida da alocação de equipamentos nas unidades educacionais. A API provê suporte para:

- Cadastro e categorização de equipamentos.
- Registro, consulta e edição de alocações.
- Acompanhamento do estado dos equipamentos (sinalização de manutenção e reporte de defeitos).

---

## ⚙️ Funcionalidades e Casos de Uso

Com base nos diagramas de caso de uso do sistema, a API atende às seguintes funcionalidades principais:

### 🎒 Gestão de Estoque (Almoxarifado)
- **Criar Categoria**: Cadastrar novas categorias para organização dos equipamentos (ex: Notebooks, Projetores, Periféricos).
- **Adicionar Equipamentos**: Registrar novos itens em quantidade no estoque do almoxarifado.
- **Acessar / Gerir Estoque**: Consultar e gerenciar a disponibilidade dos itens estocados.

### 🚚 Gestão de Alocações
- **Iniciar e Registrar Alocação**: Vincular equipamentos a uma unidade da Secretaria de Educação completando o cadastro do identificador unico : Patrimônio ou Serial (Ou ambos).
- **Visualizar Alocações**: Consultar o histórico e estado atual de alocações realizadas.
- **Editar Alocação**: Atualizar o estado de uma alocação ativa.
- **Ver / Editar Equipamento**: Detalhar especificações e atualizar o status e sinalizar condições de equipamentos alocados.
- **Sinalizar Manutenção**: Marcar equipamentos que necessitam ou estão em processo de manutenção preventiva/corretiva.
- **Reportar Defeito**: Registrar problemas técnicos e avarias identificadas nos equipamentos alocados.
- **Sinalizar descarte**: Registrar equipamentos prontos para descarte por impossibilidade de reparo.

---

## 📂 Arquitetura e Estrutura de Pastas

O projeto adota uma arquitetura em camadas bem definida (**Controller/Router → Service → Repository → Domain/Schemas**), garantindo isolamento de responsabilidades, facilidade de manutenção e facilidade para escrita de testes unitários e de integração.

```text
alocacao_equipamento/
├── domain/                     # DTOs e Schemas de validação de dados
│   └── schemas/                # Models Pydantic (Request/Response)
│       ├── categoria_equipamento_response.py
│       ├── criar_categoria.py
│       └── list_categorias.py
├── repository/                 # Camada de Acesso a Dados / Integração Supabase
│   ├── categoria_equipamento.py # Operações de banco para categorias
│   └── database.py              # Conexão e inicialização do cliente Supabase
├── service/                    # Regras de Negócio e Casos de Uso
│   └── categoria_equipamento.py # Serviços da entidade categoria
├── routers/                    # Camada HTTP / Controllers FastAPI
│   └── categoria_controller.py  # Endpoints e tratamento de rotas
├── tests/                      # Suíte de Testes da Aplicação
│   ├── integration/            # Testes de integração (Repositórios e DB)
│   │   └── test_categoria_repository.py
│   └── unity/                  # Testes unitários (Serviços e Schemas)
│       └── test_categoria_respository.py
├── main.py                     # Ponto de entrada da aplicação FastAPI
├── pyproject.toml              # Configurações do projeto e dependências
├── uv.lock                     # Lockfile gerado pelo uv (Astral)
└── README.md                   # Documentação do repositório

```


🛠️ Tecnologias Utilizadas

```text
    Linguagem: Python 3.13+

    Gerenciador de Projetos e Ambientes: uv (Astral)

    Framework Web: FastAPI

    Servidor ASGI: Granian

    Banco de Dados / Backend: Supabase (supabase-py)

    Gestão de Configurações: python-dotenv

    Suíte de Testes: pytest e pytest-cov

```

🔐 Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com as credenciais do ambiente de execução:
Snippet de código

```text
# Configurações do Supabase
EQUIP_SUPABASE_URL=[https://sua-instancia.supabase.co](https://sua-instancia.supabase.co)
EQUIP_SUPABASE_KEY=sua-chave-api-supabase
```


🚀 Instalação e Execução

Este projeto utiliza o uv como gerenciador rápido de ambientes e pacotes Python.
1. Instalar o uv (caso não possua)
```bash

curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```
2. Sincronizar Dependências
```bash

uv sync
```
3. Executar o Servidor de Desenvolvimento

A aplicação utiliza o servidor Granian:
```bash

uv run granian --interface asgi main:app --port 8000 --access-log
```
A API estará disponível por padrão em http://127.0.0.1:8000.

🧪 Execução de Testes

Os testes estão organizados em testes unitários (tests/unity) e de integração (tests/integration).
Rodar todos os testes:
```bash

uv run pytest tests/ -vv
```
Rodar testes gerando relatório de cobertura (pytest-cov):
```bash

uv run pytest tests/ -vv --cov=. --cov-report=term-missing
```
📚 Documentação da API

Com a aplicação em execução, a documentação OpenAPI gerada pelo FastAPI pode ser acessada em:

    Swagger UI: http://127.0.0.1:8000/docs

    ReDoc: http://127.0.0.1:8000/redoc

🏷️ Endpoints de Categorias (/categoria)

Abaixo estão detalhadas as rotas implementadas no controller de categorias de equipamentos (routers/categoria_controller.py):

```text
Método: POST
Rota: /categoria
Status code: 201

Headers:
Created	Cria uma nova categoria de equipamento
Location header com URI do recurso criado.
Eetorna Categoria_equipamento_response
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

Headers: No Content
```

Remove uma categoria de equipamento pelo seu ID	Sem corpo de resposta (Response vazio)

👨💻 Responsável Técnico

    Nome: Thyéz de Oliveira Monteiro

    Cargo: Assessor de Informática

    Setor: SMECICT (Tecnologia)
