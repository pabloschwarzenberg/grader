#Juego adivina mi número
from random import randint

mi_numero = randint(1,20)
intentos = 0

while intentos < 5:
	usuario = int(input("Ingresa numero: "))
	if usuario < mi_numero:
		print("mi número es mayor")
		intentos += 1
	if usuario > mi_numero:
		print("mi número es menor")
		intentos += 1
	if usuario == mi_numero:
		print("Adivinaste, mi número era", mi_numero)
		break
		
	if intentos == 5:
		print("No adivinaste, mi número era", mi_numero)