"""
EXERCÍCIO 04 — int, float e type()

Objetivo:
- Praticar operações básicas com int e float e conferir tipos com type().

Regras:
- Use print() e type().

Tarefas:
1) Crie uma variável int e uma float, some as duas e imprima o resultado.
2) Imprima o tipo (type) de cada variável e também do resultado da soma.
3) Crie duas variáveis int (ex: 7 e 2) e imprima:
   - soma
   - subtração
   - multiplicação

Dica:
- Veja: aulas/aula_4_int_float.py
"""

variavel1 = 10
variavel2 = 10.5
variavel3 = variavel1 + variavel2

print(f"O resultado da soma é: {variavel3}")
print(f"Tipo 1 = {type(variavel1)}")
print(f"Tipo 2 = {type(variavel2)}")
print(f"Tipo Resultado = {type(variavel3)}")

primeiro = 7
segundo = 2

print(primeiro + segundo)
print(primeiro - segundo)
print(primeiro * segundo)