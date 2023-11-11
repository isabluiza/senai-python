# Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

maior_peso = 0
menor_peso = 0

for contador in range (0,3):
    peso = float(input('Digite o peso em kg: '))

    if peso < menor_peso or contador == 0:
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso

print(f'\nO maior peso é de {menor_peso}kg'
      f'\nO menor peso é de {maior_peso}kg')