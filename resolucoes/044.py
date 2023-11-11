# Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder.
# Ao final deve mostrar a quantidade de vitórias

import random

impar_par = None
numero_usuario = 0
numero_maquina = 0
comparativo = 0
qnt_vitorias = 0

while True:

    impar_par = input('\nVocê deseja ser PAR ou ÍMPAR? ').upper()

    numero_usuario = int(input("\nDigite um número: "))
    numero_maquina = random.randint(1)

    comparativo = numero_usuario + numero_maquina

    if impar_par == "PAR" and comparativo % 2 == 0:
        qnt_vitorias += 1
        print(f'\nVOCÊ GANHOU!'
              f'\n São {qnt_vitorias} vitória(s)')

    elif impar_par == "IMPAR" and comparativo % 2 != 0:
        qnt_vitorias += 1
        print(f'\nVOCÊ GANHOU!'
              f'\n São {qnt_vitorias} vitória(s)')

    else:
        print(f'\nVOCÊ PERDEU!'
              f'\n São {qnt_vitorias} vitória(s)')
        break