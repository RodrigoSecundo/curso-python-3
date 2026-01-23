"""
EXERCÍCIO 05 — bool e comparações

Objetivo:
- Praticar comparações que retornam True/False.

Regras:
- Use variáveis e comparações (>, <, ==, !=, <=, >=).
- Não use if ainda.

Tarefas:
1) Crie duas variáveis (x e y) e imprima:
   - x > y
   - x == y
   - x != y

2) Faça com que UMA comparação dê True e OUTRA dê False (ajuste os valores de x e y).

3) Converta para bool:
   - um número diferente de zero
   - zero
   - uma string vazia
   - uma string não vazia
   e imprima os resultados.

Dica:
- Veja: aulas/aula_5_bool.py
"""

x = 10
y = 20

print(x > y)
print(x == y)
print(x != y)

print(x > 20)
print(y <= 20)

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Eai"))
