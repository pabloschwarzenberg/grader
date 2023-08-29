#Juego adivina mi número
print("Juego Adivina mi numero\n")
import random

numero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in range(1):
 numero_ramdo = (random.choice(numero))

contador = 0
while True:
    jugador  = int(input("Cual numero es el que piensas : "))

    if jugador == numero_ramdo:
        print("Adivinaste, mi número era " , numero_ramdo)
        break

    elif jugador > numero_ramdo:
        print("Mi numero es menor ")
        contador += 1

    elif jugador < numero_ramdo:
        print("Mi numero es mayor")
        contador += 1

    if contador == 5:
        print("No adivinaste, mi número era " , numero_ramdo)
        break