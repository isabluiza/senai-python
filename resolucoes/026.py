# Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

def calculo_imc(altura, peso):
    imc = peso / (altura * altura)

    if imc < 18.5:
        print(f'IMC: {imc:.2f}'
              '\nClassificação: Abaixo do peso')

    elif imc >= 18.5 and imc <= 24.9:
        print(f'IMC: {imc:.2f}'
              '\nClassificação: Normal')

    elif imc >= 25 and imc <= 29.9:
        print(f'IMC: {imc:.2f}'
              '\nClassificação: Sobrepeso')

    elif imc >= 30 and imc <= 34.9:
        print(f'IMC: {imc:.2f}'
              '\nClassificação: Obesidade grau I')

    elif imc >= 35 and imc <= 39.9:
        print(f'IMC: {imc:.2f}'
              '\nClassificação: Obesidade grau II')

    else:
        print(f'IMC: {imc:.2f}'
              '\nClassificação: Obesidade grau III')

altura = float(input('Digite sua altura em m: '))
peso = float(input('Digite sua peso em kg: '))

calculo_imc(altura, peso)