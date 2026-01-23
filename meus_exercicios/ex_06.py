"""
EXERCÍCIO 06 — Conversão de tipos (int, float, str, bool)

Objetivo:
- Praticar as funções int(), float(), str(), bool() com exemplos comuns.

Regras:
- Não use input().

Tarefas:
1) Converta "20" para int e some com 5. Imprima o resultado.
2) Converta "15.75" para float e some com 1.25. Imprima o resultado.
3) Converta True para int e imprima.
4) Converta 0 para bool e imprima.
5) Crie uma string "1" e um int 1 e mostre:
   - "1" + "1" (concatenação)
   - 1 + 1 (soma)
   - "1" + str(1)

Dica:
- Veja: aulas/aula_6_conversao_tipos.py
"""

print(int("20") + 5)
print(float("15.75") + 1.25)
print(int(True))
print(bool(0))
texto = "1"
numero = 1
print(texto + texto)
print(numero + numero)
print(texto + str(numero))