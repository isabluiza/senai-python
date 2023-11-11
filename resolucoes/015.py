# Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

def imp_par(num):
    validacao = num % 2
    if validacao == 0:
        print("O número é par")
    else:
        print("O número é impar")

num = float(input('Digite um numero: '))

imp_par(num)