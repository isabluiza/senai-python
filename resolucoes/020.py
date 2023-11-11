# Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

def validacao_doador_sangue(idade, peso, sono):

    if idade >= 16 and idade <= 69:
        if peso >= 50:
            if sono >= 6:
                ('\nVocê pode doar sangue!')
            else:
                print('\nVocê precisa de, pelo menos, 6h de sono para doar sangue.')
        else:
            print('\nVocê precisa pesar, pelo menos, 50kg para doar sangue.')
    else:
        print('\nVocê precisa ter, pelo menos, 6 horas de sono nas últimas 24 horas para doar sangue.')

idade = int(input('Digite sua idade: '))
peso = float(input('Digite sua peso em kg: '))
sono = int(input('Digite suas horas de sono: '))

validacao_doador_sangue(idade, peso, sono)