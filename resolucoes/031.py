# Escreva um programa que verifique se uma frase é um palíndromo.

frase = str(input('Digite uma frase: '))

validacao = frase.split()

for contador in range (0,len(validacao)):

    if validacao[contador] == validacao[-1]:
        print('sim')