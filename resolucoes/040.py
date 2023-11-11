# Escreva um programa que leia um número n inteiro qualquer
# e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci
# 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21
#   0 - 1 - 1 - 2 - 3 - 5 - 8

numero = int(input('Digite a qntd de números que você deseja saber da Sequência de Fibonacci\n'))
contador = 0
antecessor = 0
atual = 0

while contador < numero:

    if contador == 0:
        atual = 0

    if contador == 1 or contador == 2:
        antecessor = 0
        atual = 1

    proximo = antecessor + atual
    antecessor = atual
    atual = proximo

    contador += 1
    print(atual)