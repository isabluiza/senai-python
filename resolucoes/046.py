# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
#
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$1000,00
# c) Qual é o produto mais barato

produto = None
produto_mais_barato = None
preco = 0
preco_mais_barato = 0
preco_mais_caro = 0
contador_mil = 0
total = 0
continuar = None

while continuar != 'N':
    produto = input('Digite o nome do produto: ')
    preco = float(input(f'Digite o valor de {produto}: '))

    total += preco

    if preco > preco_mais_caro:
        preco_mais_caro = preco
        preco_mais_barato = preco_mais_caro

    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = produto

    if preco >= 1000:
        contador_mil += 1

    continuar = input('Deseja continuar? [S/N]\n').upper()

print(f'O valor total é R$ {total}'
      f'\n{contador_mil} custam mais que R$ 1000,00'
      f'\nO produto mais barato é o/a {produto_mais_barato}')