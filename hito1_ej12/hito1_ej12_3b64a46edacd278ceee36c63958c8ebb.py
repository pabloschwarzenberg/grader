#Juego adivina mi número
import random
numero = random.randint(1,20)
intentos = 0

while(intentos < 5):
	a = int(input("Ingrese un numero desde el 1 al 20: "))
	if (a < numero):
		print("Tu numero es menor al mio")
	elif(a > numero):
		print("Tu numero es mayor al mio")
	else:
		print("Adivinaste, mi número era",numero)
		break
	intentos += 1
if (a != numero) :
	print("No adivinaste, mi número era",numero)