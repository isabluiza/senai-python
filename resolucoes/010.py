# Escreva um programa que leia um tipo de dado e usando a método .isnumeric(), retorne ao usuário

dado= input('Digite qualquer dado: ')

verificacao = dado.isnumeric()

print(f'O dado informado é número?'
      f'\n {verificacao}')