# Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

def vog_cons(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if palavra[0] in vogais:
        print("A primeira letra é uma vogal")
    else:
        print("A primeira letra é uma consoante")

palavra = input('Digite uma palavra: ')

vog_cons(palavra)