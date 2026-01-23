"""
EXERCÍCIO 08 — Mini relatório com variáveis

Objetivo:
- Juntar print + strings + números + conversão para gerar um "relatório".

Regras:
- Não use f-string.
- Pode usar concatenação com + e str().

Tarefas:
1) Defina variáveis:
   - produto (str)
   - quantidade (int)
   - preco_unitario (float)

2) Calcule total = quantidade * preco_unitario.

3) Imprima um relatório em 3 linhas, por exemplo:
   Produto: Caneta
   Quantidade: 3
   Total: 7.5

4) Extra: mostre também o tipo de cada variável (use type()).

Dicas:
- Você pode usar print com vírgula para evitar concatenação.
- Ou pode usar concatenação e str().
"""

produto = "Notebook"
quantidade = 4
valor_unitario = 5845.89

total = valor_unitario * quantidade
print(f"""Produto: {produto}
Quantidade: {quantidade}
Valor Total: {total}""")
print()
print(type(produto))
print(type(quantidade))
print(type(valor_unitario))
print(type(total))