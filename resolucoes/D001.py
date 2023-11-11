# Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário

tempo = float(input('Informe o tempo em segundos: '))
velocidade_inicial = float(input('Informe o velocidade inicial em m/s: '))
velocidade_final = float(input('Informe o velocidade final em m/s: '))
posicao_inicial = float(input('Informe o posição inicial em m: '))

aceleracao = (velocidade_final-velocidade_inicial)/tempo

posicao = posicao_inicial + velocidade_inicial * tempo + ((aceleracao*(tempo**2))/2)

print(f'A posição do objeto no tempo {tempo} é de {posicao}m')

