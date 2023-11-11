# Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

def pos_neg(num):
    if num < 0:
        print("O número é negativo")
    else:
        print("O número é positivo")

num = float(input('Digite um numero: '))

pos_neg(num)

