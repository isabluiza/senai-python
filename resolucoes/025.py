# Crie um programa para jogar JOKEMPO, usando a função random.randint
import random

Escolha_jogador = int(input('\n Digite uma das seguintes opções: '
                    '\n1 - Pedra'
                    '\n2 - Papel'
                    '\n3 - Tesoura'
                    '\n Qual a sua escolha? '))

Escolha_PC = random.randint(1,3)

if Escolha_jogador > 3 or Escolha_jogador < 1:
    print('Escolha inválida')
else:
    if Escolha_PC == Escolha_jogador:
        print('Empatamos - Foi por Pouco')

    elif Escolha_PC == 1 and Escolha_jogador == 3:
        print('Pedra x Tesoura'
              '\nEu Ganhei')

    elif Escolha_PC == 2 and Escolha_jogador == 1:
        print('Papel x Pedra'
              '\nEu Ganhei')

    elif Escolha_PC == 3 and Escolha_jogador == 2:
        print('Tesoura x Papel'
              '\nEu Ganhei')

    else:
        if Escolha_PC == 1:
            Escolha_PC = 'Pedra'
        elif Escolha_PC == 2:
            Escolha_PC = 'Papel'
        else:
            Escolha_PC = 'Tesoura'

        if Escolha_jogador == 1:
            Escolha_jogador = 'Pedra'
        elif Escolha_jogador == 2:
            Escolha_jogador = 'Papel'
        else:
            Escolha_jogador = 'Tesoura'

        print(f'Escolha PC: {Escolha_PC} X {Escolha_jogador}, Você Ganhou')
