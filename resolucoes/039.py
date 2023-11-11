# Faça um programa que leia um número e retorne o fatorial !

numero = int(input('Digite um número para saber seu fatorial:'))
fatorial = numero - 1

while fatorial != 1:
    numero = numero * fatorial
    fatorial -= 1

print(numero)