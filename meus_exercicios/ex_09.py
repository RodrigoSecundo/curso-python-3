"""
EXERCÍCIO 09 — Desafio de formatação com print

Objetivo:
- Treinar sep e end para construir uma saída exatamente do jeito pedido.

Regras:
- Use apenas print().

Tarefas:
1) Faça o programa imprimir exatamente:
   [A]-[B]-[C]
   usando 1 único print e sep='-'.

2) Faça o programa imprimir exatamente (mesma linha):
   Início...meio...fim
   usando 3 prints (dica: controle o end).

3) Faça o programa imprimir as duas linhas abaixo com DOIS prints:
   Nome: Ana
   Idade: 20

Dica:
- Veja: aulas/aula_2_funcao_print.py
"""

print("[A]", "[B]", "[C]", sep="-")

print("Início ...", end="")
print(" meio ...", end="")
print(" fim")

print("Nome: Ana")
print("Idade: 20")