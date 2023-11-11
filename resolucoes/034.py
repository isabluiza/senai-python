# Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma

num_final = 0

for contador in range(0,10):
	num = float(input('Digite um numero: '))
	if num % 2 == 0:
		num_final += num

print(num_final)