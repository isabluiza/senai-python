# Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

num_inicial = int(input('Digite o número inicial: '))
num_final = int(input('Digite o número final: '))

for contador in range (num_inicial, num_final+1):
    if contador % 2 == 0:
        print(contador)