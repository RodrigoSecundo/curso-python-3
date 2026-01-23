"""
EXERCÍCIO 01 — print(), sep e end

Objetivo:
- Praticar a função print com múltiplos argumentos, e os parâmetros sep= e end=.

Regras:
- Use apenas print() (e sep/end). Não use input(), if, loops, etc.

Tarefas:
1) Imprima: 56 e 78 na mesma linha, SEM espaço entre eles.
2) Imprima 3 palavras (você escolhe) separadas por ' | ' (com espaços).
3) Imprima duas linhas usando apenas um print (dica: use \n dentro da string).
4) Imprima "FIM" sem quebrar linha no final (use end='').

Dica:
- Veja a aula sobre print: aulas/aula_2_funcao_print.py
"""

print(56, 78, sep="")
print("Rodrigo", "Secundo", "Araújo", sep=" | ")
print("Isso é: \nbom")
print("FIM", end="")
print("Prova que não quebrou")