# Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média
# é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

soma = 0
nota = 0
contador = 0

for contador in range(0,4):
    nota = float(input('Digite a nota: '))
    soma += nota
    contador += 1

media = soma/5

if media < 6:
    print(f'Sua média de {media} é insuficiente')

elif media > 6 and media < 7:
    print(f'Sua média de {media} é suficiente')

elif media > 7 and media < 9:
    print(f'Sua média de {media} é bom')

elif media >= 9:
    print(f'Sua média de {media} é excelente')