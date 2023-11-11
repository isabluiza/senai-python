# Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500

num_final = 0

for num in range(1,501):
	if num % 4 == 0:
		num_final += num

print(num_final)