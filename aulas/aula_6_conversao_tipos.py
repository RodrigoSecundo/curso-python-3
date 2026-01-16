# A conversão de tipos em Python permite transformar um valor de um tipo de dado para outro.
# Isso é útil quando precisamos realizar operações que exigem tipos específicos.
# As funções principais para conversão de tipos são: int(), float(), str(), bool()

# Conversão para inteiro
print(int(10.5))    # Converte float para int, resultado: 10
print(int("20"))    # Converte string para int, resultado: 20
print(int(True))    # Converte bool para int, resultado: 1
print(int(False))   # Converte bool para int, resultado: 0

# Conversão para float
print(float(10))      # Converte int para float, resultado: 10.0
print(float("15.75")) # Converte string para float, resultado: 15.75
print(float(True))    # Converte bool (True = 1) para float, resultado: 1.0
print(float(False))   # Converte bool (False = 0) para float, resultado: 0.0

# Conversão para string
print(str(100))       # Converte int para string, resultado: "100"
print(str(25.5))      # Converte float para string, resultado: "25.5"
print(str(True))      # Converte bool para string, resultado: "True"
print(str(False))     # Converte bool para string, resultado: "False"

# Conversão para booleano
print(bool(1))        # Converte int para bool, resultado: True
print(bool(0))        # Converte int (0 = false) para bool, resultado: False
print(bool(3.14))     # Converte float para bool, resultado: True
print(bool(0.0))      # Converte float (0 = false) para bool, resultado: False
print(bool("Hello"))  # Converte string para bool, resultado: True
print(bool(""))       # Converte string vazia para bool, resultado: False

# A concatenação de strings com diferentes tipos requer conversão explícita

print( 1 + 1 )        # Soma de inteiros, resultado: 2
print( "1" + "1" )    # Concatenação de strings, resultado: "11"
# print( "1" + 1 )    # Isso causaria um erro de tipo, python só permite concatenar um tipo com ele mesmo, por isso aprendemos a converter tipos
print( "1" + str(1) ) # Concatenação após conversão, resultado: "11"
# Vale lembrar que a conversão nem sempre é possível
# print(int("uai?"))    # Isso causaria um erro, pois "uai?" não pode ser convertido para int
# print(float("dez"))   # Isso causaria um erro, pois "dez" não pode ser convertido para float

# Ou seja, números podem ser convertidos em strings, mas strings nem sempre podem ser convertidas em números.