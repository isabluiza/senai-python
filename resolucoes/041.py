# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

opcao = ''
soma = 0
media = 0
maior_num = 0
menor_num = 0
contador = 0

while opcao != 'N':
    numero = int(input('Digite um número para a comparação:\n'))

    if numero > maior_num:
        maior_num = numero
        menor_num = maior_num

    if numero < menor_num:
        menor_num = numero

    soma = soma + numero

    opcao = input('Deseja inserir mais um número? (S/N)\n').upper()
    contador += 1

media = soma / contador

print(f'A média entre os números digitados é {media}')
print(f'O menor número entre os números digitados é: {menor_num}')
print(f'O maior número entre os números digitados é: {maior_num}')
