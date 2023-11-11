# Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123")

def validacao_senha(senha):

    if senha == "python123":
        print('Login válido')
    else:
        print('Digite novamente.')

senha = input('Digite sua senha: ')
validacao_senha(senha)