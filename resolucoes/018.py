# Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).

def maioridade(idade):
    if idade >= 18:
        print('Você é maior de idade')
    else:
        print('Você é menor de idade')

idade = int(input('Digite sua idade: '))

maioridade(idade)