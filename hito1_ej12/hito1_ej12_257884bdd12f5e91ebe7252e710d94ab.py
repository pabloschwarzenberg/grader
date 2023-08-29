import random 
numeroAleatorio = random.randint(1,20)
intentos = 5
while True:
	eleccion = int(input("adivina un numero del 1 al 20 : "))
	intentos -= 1
	if intentos <= 0:
		print("no adivinaste, mi numero era: ", numeroAleatorio)
		break
	if eleccion == numeroAleatorio:
		print("adivinaste!, mi numero era: ", numeroAleatorio)
		break
	if eleccion > numeroAleatorio:
		print("mi numero es menor")
	else:
		print("mi numero es mayor")