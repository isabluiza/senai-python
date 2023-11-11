# Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

def vog_cons(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if letra in vogais:
        print("Essa letra é uma vogal")
    else:
        print("Essa letra é uma consoante")

letra = input('Digite uma letra: ')

vog_cons(letra)