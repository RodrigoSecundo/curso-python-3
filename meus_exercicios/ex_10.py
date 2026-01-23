"""
EXERCÍCIO 10 — Desafio: adivinhe o tipo

Objetivo:
- Fixar diferenças entre int, float, str e bool e como o Python trata conversões.

Regras:
- Use print() e type().

Tarefas:
1) Sem rodar (primeiro no papel), tente adivinhar o tipo de cada expressão.
2) Depois rode e confira com type().

Expressões:
- 10
- 10.0
- "10"
- int("10")
- float("10")
- bool("10")
- bool("")
- int(True)
- float(False)
- "1" + "1"
- 1 + 1

Dica:
- Veja: aulas/aula_4_int_float.py, aulas/aula_5_bool.py, aulas/aula_6_conversao_tipos.py
"""

print(type(10))
print(type(10.0))
print(type("10"))
print(type(int("10")))
print(type(float("10")))
print(type(bool("10")))
print(type(bool("")))
print(type(int(True)))
print(type(float(False)))
print(type("1" + "1"))
print(type(1 + 1))