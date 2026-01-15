# O tipo bool representa valores booleanos, que podem ser apenas True (verdadeiro) ou False (falso).
# Esses valores são usados principalmente em estruturas de controle e condições.

print(True)   # Exibe o valor booleano True
print(False)  # Exibe o valor booleano False
print(type(True))   # type verifica o tipo do valor, se colocado em print exibe o tipo na tela
print(type(False))  # type verifica o tipo do valor, se colocado em print exibe o tipo na tela

# Valores booleanos são frequentemente o resultado de expressões de comparação
print(10 > 5)    # Exibe True, pois 10 é maior que 5
print(3 == 4)    # Exibe False, pois 3 não é igual a 4
print(7 <= 7)    # Exibe True, pois 7 é menor ou igual a 7
print(2 != 2)    # Exibe False, pois 2 é igual a 2

# Também é possível converter outros tipos para bool usando a função bool()
print(bool(1))      # Exibe True, pois 1 é considerado verdadeiro
print(bool(0))      # Exibe False, pois 0 é considerado falso
print(bool(-5))     # Exibe True, qualquer número diferente de zero é considerado verdadeiro
print(bool(""))     # Exibe False, string vazia é considerada falsa
print(bool("Olá"))  # Exibe True, string não vazia é considerada verdadeira
print(bool([]))     # Exibe False, lista vazia é considerada falsa
print(bool([1, 2])) # Exibe True, lista não vazia é considerada verdadeira
# por aí vai...

# Valores booleanos são amplamente utilizados em estruturas de controle como if, while, etc. Mais para frente veremos exemplos práticos disso.