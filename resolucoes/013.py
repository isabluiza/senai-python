'''
Crie um programa que leia uma frase e mostre:
1. Quantas vezes aparece a letra “a”
2. Em que posição ela aparece a primeira vez
3. Em que posição ela aparece na última vez
'''

frase = input('Digite uma frase: ')

print(f'A letra "a" aparece {frase.lower().count("a")} vezes'
      f'\nA letra primeira letra "a" aparece na posição {frase.find("a") + 1}'
      f'\nA letra primeira letra "a" aparece na posição {frase.find("a", -1) + 1}')

