# Projeto de Validacao de Qualidade de Codigo Python (PEP 8)

Este repositorio foi criado para praticar padronizacao de codigo Python com foco em PEP 8, automacao de formatacao e verificacoes de qualidade antes do commit.

## Objetivo

Padronizar e validar scripts Python que processam dados de temperatura, usando ferramentas de lint e formatacao integradas ao fluxo de desenvolvimento.

## O Que Existe no Projeto

- `teste_final.py`: implementacao base para leitura e agregacao de temperaturas por estacao.
- `teste_flake8.py`: versao orientada a conformidade de estilo e boas praticas de lint.
- `teste_black.py`: versao para exercitar formatacao automatica com Black.
- `teste_blue.py`: experimento de consulta agregada com DuckDB.
- `.pre-commit-config.yaml`: pipeline de validacao automatica antes do commit.
- `.flake8`: regras de lint do projeto.
- `pyproject.toml`: dependencias e configuracoes do Poetry/isort/taskipy.

## Stack de Qualidade

- `flake8` para analise estatica de estilo.
- `black` para formatacao automatica.
- `isort` para organizacao de imports.
- `pre-commit` para executar hooks localmente antes de cada commit.
- `taskipy` para facilitar execucao de tarefas.

## Requisitos

- Python `3.12.1` (arquivo `.python-version`).
- Poetry instalado no ambiente.

## Setup Rapido

1. Instale as dependencias:

```bash
poetry install
```

2. Ative os hooks do pre-commit:

```bash
poetry run pre-commit install
```

3. Rode a validacao completa:

```bash
poetry run pre-commit run --all-files
```

## Como Executar os Scripts

Os scripts esperam um arquivo em `data/measurements.txt`.

```bash
poetry run python teste_final.py
poetry run python teste_flake8.py
poetry run python teste_black.py
poetry run python teste_blue.py
```

## Comandos Uteis

Validacao completa com hooks:

```bash
poetry run pre-commit run --all-files
```

Rodar somente flake8:

```bash
poetry run flake8 .
```

Rodar tarefa configurada no Taskipy:

```bash
poetry run task format
```

## Diagnostico Atual do Projeto

- O fluxo de qualidade ja esta automatizado com `pre-commit`.
- O README anterior estava desatualizado (citava apenas `teste.py`).
- O repositorio esta organizado como ambiente de estudo de qualidade de codigo e processamento de dados.

## Proximos Passos Recomendados

- Adicionar Bandit ao pipeline para analise de seguranca.
- Consolidar as versoes dos scripts em uma estrutura unica (ex.: pasta `src/`).
- Criar testes automatizados para validar o comportamento funcional.
