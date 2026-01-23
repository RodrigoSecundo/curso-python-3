"""
EXERCÍCIO 07 — Variáveis e cálculos simples

Objetivo:
- Praticar criação/atualização de variáveis e usar valores em contas.

Regras:
- Use variáveis, operações e print().

Tarefas:
1) Crie variáveis: nome (str), idade (int), altura (float).
2) Imprima cada uma.
3) Calcule o ano de nascimento considerando o ano atual como 2026.
   (ano_nascimento = 2026 - idade)
4) Atualize a idade (ex: +1) e imprima novamente.

Dica:
- Veja: aulas/aula_7_introducao_variaveis.py
"""

nome = "Rodrigo"
idade = 22
altura = 1.80

print(nome)
print(idade)
print(f"{altura:.2f}")

ano_nascimento = 2026 - idade
print(ano_nascimento)

idade += 1
print(idade)