'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1. O nome com todas as letras maiúsculas
2. O nome com todas minúsculas
3. Quantas letras ao todo (sem considerar os espaços)
4. Quantas letras tem o primeiro nome
'''

nome_completo = input('Digite seu nome completo: ')

print(f'Nome maiúsculo: {nome_completo.upper()}'
      f'\nNome minúsculo: {nome_completo.lower()}'
      f'\nQuantidade letras: {len(nome_completo.replace(" ",""))}'
      f'\nO primeiro nome tem {len(nome_completo.split()[0])} caracteres')