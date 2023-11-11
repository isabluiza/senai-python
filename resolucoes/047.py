# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
#
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

saque = 0
contador_50 = 0
contador_20 = 0
contador_10 = 0
contador_1 = 0

saque = int(input('\nDigite o valor a ser sacado: '))

while saque >= 50:
    saque -= 50
    contador_50 += 1

while saque <= 50 and saque >= 20:
    saque -= 20
    contador_20 += 1

while saque <= 20 and saque >= 10:
    saque -= 10
    contador_10 += 1

while saque < 10 and saque > 0:
    saque -= 1
    contador_1 += 1

print(f'\nSerão entregues:'
      f'\n {contador_50} célula(s) de R$ 50'
      f'\n {contador_20} célula(s) de R$ 20'
      f'\n {contador_10} célula(s) de R$ 10'
      f'\n {contador_1} célula(s) de R$ 1')