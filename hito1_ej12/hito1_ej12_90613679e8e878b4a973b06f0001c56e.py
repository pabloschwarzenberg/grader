#Juego adivina mi número
import random

x =random.randrange(1, 20)
intento = 0
while intento <= 4 or tri == x:
    intento += 1
    tri= int(input("¿que numero crees que es?"))
    if tri == x:
        print("Adivinaste, mi numero era", x)
    elif tri > x:
        print("Mi numero es menor")
    elif tri < x:
        print("Mi numero es mayor")
    if intento == 5 and tri != x:
        print("No adivinaste, mi numero era", x)      