# 📦 API de Alocação de Equipamentos e Controle de Estoque (Secretaria de Educação)

**Versão:** 0.8.1

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
├── domain
│   ├── enums.py
│   ├── __pycache__
│   │   └── enums.cpython-313.pyc
│   └── schemas
│       ├── __pycache__
│       │   └── schemas.cpython-313.pyc
│       └── schemas.py
├── main.py
├── __pycache__
│   └── main.cpython-313.pyc
├── pyproject.toml
├── README.md
├── repository
│   ├── database.py
│   ├── repository_alocacao.py
│   ├── repository_categoria.py
│   ├── repository_equipamento.py
│   └── repository_historico.py
├── routers
│   ├── controller_alocacao.py
│   ├── controller_categoria.py
│   └── controller_historico.py
├── service
│   ├── service_alocacao.py
│   ├── service_categoria_equipamento.py
│   └── service_historico_equipamento.py
├── tests
│   ├── 1_unity
│   │   ├── test_service_alocacao.py
│   │   ├── test_service_categoria.py
│   │   └── test_service_historico.py
│   ├── 2_integration
│   │   ├── test_repository_alocacao.py
│   │   ├── test_repository_categoria.py
│   │   ├── test_repository_equipamento.py
│   │   └── test_repository_historico.py
│   └── 3_e2e
│       ├── test_e2e_alocacao.py
│       ├── test_e2e_categoria.py
│       ├── test_e2e_equipamento.py
│       └── test_e2e_historico.py
└── uv.lock
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

ou

pip install uv
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

Os testes estão organizados em testes unitários (`tests/1_unity`), de integração (`tests/2_integration`) e testes de fluxo ponta-a-ponta (`tests/3_e2e`).
Rodar todos os testes:
```bash

uv run pytest tests/ -vv
```
Rodar testes gerando relatório de cobertura (pytest-cov):
```bash

uv run pytest tests/ -vv --cov=. --cov-report=term-missing
```

## Documentação

Temos as documentações detalhadas de cada domínio de recursos:
- [Documentação de Categorias](docs/endpoints/categorias.md)
- [Documentação de Históricos](docs/endpoints/historicos.md)
- [Documentação de Equipamentos](docs/endpoints/equipamentos.md)
- [Documentação de Alocações](docs/endpoints/alocacoes.md)

---

👨💻 Responsável Técnico

    Nome: Thyéz de Oliveira Monteiro
    Cargo: Assessor de Informática
    Setor: SMECICT (Tecnologia - Sala 25)
