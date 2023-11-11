# Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

def validacao_intervalo(num):
    if num >= 0 and num <= 10:
        print('Seu número está entre 0 e 10')
    elif num > 10 and num < 20:
        print('Seu número está entre 10 e 20')
    elif num >= 20:
        print('Seu número é maior que 20')
    else:
        print('Seu número é menor que zero')

num = int(input('Digite um número: '))

validacao_intervalo(num)