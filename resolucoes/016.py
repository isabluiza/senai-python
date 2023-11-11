# Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

def igual_diferente(num1,num2):
    if num1 == num2:
        print("Eles são iguais")
    else:
        print("Eles são diferentes")

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))

igual_diferente(num1,num2)