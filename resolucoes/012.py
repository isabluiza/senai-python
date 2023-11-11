# Crie um programa que leia um nome, e mostre o primeiro e o último nome

nome_completo = input('Digite seu nome completo: ').strip

print(f'Primeiro nome: {nome_completo.split()[0]}'
      f'\nÚltimo nome: {nome_completo.split()[-1]}')