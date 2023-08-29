#Juego adivina mi número
import random
numero=random.randint(0, 20)
print("Numero generado, comenzemos ")

for a in range(5):
	ni=int(input("Ingrese numero: "))
	
	if ni > numero:
		print("Tu numero es mayor ")
	elif ni < numero:
		print("Tu numero es menor ")
	else:
		print("Adivinaste, mi numero era: " + str(numero))
print("No adivinaste mi numero era: " + str(numero))
