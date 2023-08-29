#Juego adivina mi número
import random
numero= random.randint(1,20)
intentos = 0
while intentos < 5:
    numeroad = int(input("Ingresa tu numero: "))
    intentos = intentos+1
    if (numeroad < numero):
        print("mi numero es mayor")
    if (numeroad>numero):
        print("mi numero es menor")
    if (numeroad==numero):
        break
if numeroad == numero:
    print("Adivinaste, mi número era",numero)
if numeroad != numero:
    print("No adivinaste, mi número era",numero)      