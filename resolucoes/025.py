# Crie um programa para jogar JOKEMPO, usando a função random.randint

import random

jogador = int(input('\n Digite uma das seguintes opções: '
                    '\n1 - Pedra'
                    '\n2 - Papel'
                    '\n3 - Tesoura\n'))

maquina = random.randint(1,3)

if jogador > 3 or jogador < 1:
    print('Escolha inválida')

else:
    if maquina == jogador:
        print('Empatamos. Ninguém ganhou')

    elif maquina == 1 and jogador == 3:
        print('Pedra x Tesoura'
              '\nEu ganhei!')

    elif maquina == 2 and jogador == 1:
        print('Papel x Pedra'
              '\nEu ganhei!')

    elif maquina == 3 and jogador == 2:
        print('Tesoura x Papel'
              '\nEu ganhei!')

    else:
        if maquina == 1:
            maquina = 'Pedra'

        elif maquina == 2:
            maquina = 'Papel'

        else:
            maquina = 'Tesoura'

        if jogador == 1:
            jogador = 'Pedra'

        elif jogador == 2:
            jogador = 'Papel'

        else:
            jogador = 'Tesoura'

        print(f'{maquina} X {jogador}. Você ganhou!')
