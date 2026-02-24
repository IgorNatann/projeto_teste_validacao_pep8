# projeto_teste_validacao_pep8

## Correcoes aplicadas de PEP8

Foram aplicadas as seguintes correcoes no arquivo `teste.py`:

- `E302`: garantidas 2 linhas em branco entre definicoes de alto nivel.
- `E501`: quebradas linhas acima de 79 caracteres (atribuicoes, compreensao
  de dicionario e `print` final).
- `W292`: garantida quebra de linha no fim do arquivo.

## Como validar

1. Instale as dependencias do projeto.
2. Execute:

```bash
flake8 teste.py
```
