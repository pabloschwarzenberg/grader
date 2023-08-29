from random import randint

if __name__ == '__main__':
	intentos = 5
	num_secreto = int(randint(0,99)+1)
	print("Adivine el numero (de 0 a 100):")
	num_ingresado = int(input())
	while num_secreto != num_ingresado and intentos>1:
		if num_secreto > num_ingresado:
			print("Muy bajo")
		else:
			print("Muy alto")
		intentos = intentos-1
		print("Le quedan ",intentos," intentos:")
		num_ingresado = float(input())
	if num_secreto==num_ingresado:
		print("Adivinaste, mi número era ", num_secreto)
	else:
		print("El numero era: ",num_secreto)


