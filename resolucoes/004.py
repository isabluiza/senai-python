# Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

raio = float(input('Digite o raio da esfera: '))

pi = 3.14

volume = (4/3) * pi * (raio**3)
area = 4 * pi * (raio**2)

print(f'Volume da Esfera: {volume}')
print(f'Área da Esfera: {area}')