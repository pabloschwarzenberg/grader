#Juego adivina mi número
from random import randint

numeroSecreto = randint(1,20)

intentos = 1
while intentos <= 5 :
	numeroEscogido = int(input("Adivina el número: "))
	if numeroEscogido == numeroSecreto :
		print ("Adivinaste mi numero era",numeroSecreto)
		intentos = 5
	else :
		print ("Incorrecto")
	intentos = intentos + 1
if numeroEscogido != numeroSecreto :
        print ("No adivinaste, mi número era:", numeroSecreto)