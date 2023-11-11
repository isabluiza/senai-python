# Crie um programa que retorne a tabuada de um número,
# e só pare quando o número digitado for 0000

numero = 0
multiplicador = 0
resultado = 0

while True:
    multiplicador = 0

    numero = float(input('\nDigite um número para saber sua tabuada:'
                         '\n Para sair do programa, digite "0000" '))

    if numero == 0000:
        print("\n ----- VOCÊ SAIU DO PROGRAMA ----- ")
        break

    while multiplicador != 11:

        resultado = numero * multiplicador
        print(f'\n\n{numero} * {multiplicador} = {resultado}')

        multiplicador += 1

