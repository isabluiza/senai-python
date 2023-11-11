# Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico,
# permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair

opcao = 0
saldo = 0
deposito = 0
saque = 0

while opcao != 4:

    opcao = int(input('\n\nEscolha a operação que deseja seguir:'
                      '\n1. Fazer depósito'
                      '\n2. Fazer saque'
                      '\n3. Consultar saldo'
                      '\n4. Finalizar\n'))

    if opcao == 1:
        deposito = float(input('Digite o valor a ser depositado na conta: '))
        saldo = saldo + deposito

    elif opcao == 2:
        saque = float(input('Digite o valor a ser sacado da conta: '))
        saldo = saldo - saque

    elif opcao == 3:
        print(f'Seu saldo é de: R$ {saldo}')