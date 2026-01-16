# Variáveis em Python são usadas para armazenar valores que podem ser usados e manipulados ao longo do código.
# Uma variável é criada ao atribuir um valor a um nome usando o operador de atribuição (=).
# Segundo o PEP 8, que é o guia de estilo para Python, os nomes das variáveis devem ser descritivos e usar letras minúsculas com palavras separadas por underscores (_).
# O uso seria algo como: nome_da_variavel = valor

# Exemplo de criação e uso de variáveis
idade = 25               # Variável do tipo inteiro
altura = 1.75           # Variável do tipo float
nome = "João"           # Variável do tipo string   
estudante = True        # Variável do tipo booleano
print(idade)            # Exibe o valor da variável idade
print(altura)           # Exibe o valor da variável altura
print(nome)             # Exibe o valor da variável nome
print(estudante)        # Exibe o valor da variável estudante

# Podemos usar variáveis em expressões e operações
ano_nascimento = 2024 - idade  # Calcula o ano de nascimento
print(ano_nascimento)           # Exibe o ano de nascimento

# Podemos atualizar o valor de uma variável atribuindo um novo valor a ela
idade = 26                     # Atualiza a variável idade
print(idade)                   # Exibe o novo valor da variável idade

# Nomes de variáveis devem seguir algumas regras:
# 1. Devem começar com uma letra (a-z) ou um underscore (_)
# 2. Podem conter letras, números (0-9) e underscores (_)
# 3. Não podem ser palavras reservadas do Python (como if, else, while, etc.)
# 4. São sensíveis a maiúsculas e minúsculas (idade e Idade são variáveis diferentes, mesmo que o recomendado seja usar apenas minúsculas para variáveis)
# 5. Devem ser descritivos para facilitar a leitura do código