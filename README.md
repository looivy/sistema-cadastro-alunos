# Sistema de Cadastro de Alunos

Programa em Python com menu interativo para gerenciar alunos: cadastro, listagem, busca, remoção e cálculo de média das notas.

## Funcionalidades

- Cadastrar aluno: nome, idade e 3 notas (a média é calculada automaticamente)
- Listar alunos: exibe todos os alunos cadastrados
- Buscar aluno: busca por nome completo ou parcial
- Remover aluno: remove pelo nome completo
- Mostrar média: exibe a média de um aluno específico

## Conceitos aplicados

- Estruturas de dados: lista de dicionários
- match/case para o menu de opções
- Tratamento de exceções (try/except) para entradas inválidas
- Loop for/else para busca e validação de existência
- Formatação de string (f-strings)

## Como executar

```bash
python3 cadastro_alunos.py
```

## Possíveis melhorias futuras

 1. Persistência de dados em arquivo JSON
 2. Refatoração para POO (classes Aluno e Sistema)
 3. Testes automatizados com pytest
 4. Validação de idade e notas (ex: nota entre 0 e 10)

---

**Projeto desenvolvido como parte dos estudos de Python**