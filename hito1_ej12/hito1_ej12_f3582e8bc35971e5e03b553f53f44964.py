#Juego adivina mi número
import random
numero=random.randint(1,20)
i=0
while i<5:
    jugador=int(input())
    if jugador<numero:
        print("mi numero es mayor")
    if numero<jugador:
        print("mi numero es menor")
    if numero==jugador:
        print("Adivinaste, mi numero era", numero)
    i+=1
print("No adivinaste, mi numero era", numero)