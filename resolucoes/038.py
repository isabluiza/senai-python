# Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

# 1.	Somar
# 2.	Multiplicar
# 3.	Maior
# 4.	Novos números
# 5.	Sair do programa

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

opcao = 0
resultado = 0

while opcao != 5:
    opcao = int(input('\n\nQUAL OPERAÇÃO DESEJA REALIZAR?'
                      '\n 1. Somar'
                      '\n 2. Multiplicar'
                      '\n 3. Maior'
                      '\n 4. Novos números'
                      '\n 5. Sair do programa\n'))

    if opcao == 1:
        resultado = num1 + num2 + num3
        print(f'\nEsse é o resultado da soma de {num1} + {num2} + {num3} = {resultado}')

    elif opcao == 2:
        resultado = num1 * num2 * num3
        print(f'\nEsse é o resultado da soma de {num1} * {num2} * {num3} = {resultado}')

    elif opcao == 3:
        if num1 > num2 and num1 > num3:
            print(f'\nO maior número entre os três é {num1}')
        elif num2 > num3 and num2 > num3:
            print(f'\nO maior número entre os três é {num2}')
        else:
            print(f'\nO maior número entre os três é {num3}')

    elif opcao == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        num3 = float(input('Digite o terceiro número: '))