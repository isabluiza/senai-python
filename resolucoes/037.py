# Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10
# e continue pedindo até que o usuário acerte o número.
# E no final, retorne também a quantidade de tentativas necessárias.

import random

numero = random.randint(1,10)
resposta = 0

while resposta != numero:
    resposta = int(input('Tente acertar o número inteiro misterioso digitando de 1 a 10\n'))

print(f'Você acertou o número! É {numero}!')