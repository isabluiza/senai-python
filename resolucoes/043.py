# Crie um programa que leia vários números inteiros.
# O programa só vai parar quando o usuário digitar 0000.
# No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

numero = 0
soma = 0
qnt_numeros = -1

print('\nPara sair do programa, digite "0000"')

while True:
    numero = int(input('\nDigite um número inteiro: '))
    soma = soma + numero
    qnt_numeros += 1
    if numero == 0000:
        print(f"\nForam digitados {qnt_numeros} números "
              f"\ne a soma deles é {soma}"
              "\n\n ----- FIM DO PROGRAMA ----- ")
        break