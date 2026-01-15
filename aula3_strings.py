# Strings devem estar entre aspas simples ou duplas, tendo obrigação apenas de serem iguais no início e no fim
# As duas formas são equivalentes e podem ser usadas conforme preferência
print('Olá, mundo!')
print("Bem-vindo ao Python!")
# print('Ele disse "Oi!") # daria erro por causa das aspas diferentes
print('Ele disse "Oi!"')  # correto, umas aspas dentro das outras é permitido, sendo a externa a que define a string

# No entanto também é possível usar o caractere de escape \ para incluir aspas dentro da string
print("Ele disse \"Oi!\"")  # correto, aspas duplas dentro de aspas duplas com escape
# Mas é muito mais trabalhoso usar o caractere de escape, então prefira usar aspas diferentes quando possível

# Também é possível exibir o caractere de escape usando o r prefixo
print(r"Ele disse \"Oi!\"")  # o r antes das aspas indica que é uma raw string, onde escapes não são processados

# Você também pode usar aspas triplas para strings de múltiplas linhas
print("""Esta é uma string
de múltiplas linhas.""")