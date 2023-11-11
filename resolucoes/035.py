# Escreva um programa que leia o
# Nome, idade e sexo de 4 pessoas. No final mostre:
# 1. A média de idade do grupo
# 2. Qual é o homem mais velho
# 3. Quantas mulheres têm menos de 20 anos

media = 0
contador = 0
soma_idade = 0
nome_do_homem = "Nenhum homem"
idade_do_homem = 0
contador_mulheres = 0

for contador in range(0,3):
    nome = str(input('Digite a nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite "F" para feminino; "M" para masculino: '))

    if sexo.upper() == "M" and idade > idade_do_homem:
        idade_do_homem = idade
        nome_do_homem = nome

    if sexo.upper() == "F" and idade > 20:
        contador_mulheres += 1

    soma_idade += idade

media = soma_idade / (contador+1)

print (f'\n\nA média entre as idades é {media}')
print (f'{nome_do_homem} é o nome do homem mais velho')
print (f'A quantidade de mulheres abaixo dos 20 anos é {contador_mulheres}')
