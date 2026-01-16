# A função print é usada para exibir mensagens na tela

print("Qualquer coisa") # texto entre aspas é uma string
print(1234) # números são exibidos como estão
print(10 + 5) # expressões matemáticas são avaliadas antes de exibir o resultado
print("A soma de 10 + 5 é:", 10 + 5) # múltiplos argumentos são separados por vírgulas
# print("Oi" + 5) # dará erro, pois não se pode concatenar string com número diretamente
print("Oi" + str(5)) # converte o número 5 para string antes de concatenar, por exemplo
print( 56, 78, sep="") # o argumento sep define o separador entre múltiplos argumentos, por padrão é um espaço se não definido
print(56, 78, end=" FIM") # o argumento end define o que é colocado no final da impressão, por padrão é uma nova linha (\n)
print("Linha 1\nLinha 2") # \n insere uma nova linha

# Existem muitas outras particularidades sobre a função print que serão vistas mais adiante