'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1. O nome com todas as letras maiúsculas
2. O nome com todas as letras minúsculas
3. Quantas letras ao todo (sem considerar os espaços)
4. Quantas letras tem o primeiro nome

OBS: Tratar os espaços extras entre os nomes
'''

nome_completo = input('Digite seu nome completo: ')

print(f'Nome maiúsculo: {nome_completo.upper()}')
print(f'Nome minúsculo: {nome_completo.lower()}')

print(f'Quantidade letras: {len(nome_completo.strip().replace(" ",""))}')

print(f'O primeiro nome tem {len(nome_completo.split()[0])} caracteres')

