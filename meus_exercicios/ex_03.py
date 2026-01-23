"""
EXERCÍCIO 03 — Concatenação e conversão para str

Objetivo:
- Praticar concatenação de strings e conversão de números para string.

Regras:
- Não use f-string ainda; use concatenação com + e/ou print com múltiplos argumentos.
- Você pode usar str().

Tarefas:
1) Faça o programa imprimir: "Eu tenho 3 cachorros".
   Você deve ter um número em uma variável (int) e converter quando necessário.

2) Faça o programa imprimir: "O preço é R$ 19.9".
   Use uma variável float.

3) Sem usar +, imprima na mesma linha: "Soma:" e o resultado de 10 + 5.

Dica:
- Veja: aulas/aula_2_funcao_print.py e aulas/aula_6_conversao_tipos.py
"""

# Crie as variáveis que você vai usar.
quantidade_cachorros = 3
preco = 19.9
soma = 10 + 5

print(f"Eu tenho {quantidade_cachorros} cachorros")
print(f"O preço é R$ {preco:.2f}")
print(f"Soma: {soma}")