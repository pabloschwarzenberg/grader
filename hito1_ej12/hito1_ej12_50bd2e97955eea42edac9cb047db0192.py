#Juego adivina mi número
import random 

contador = 0

r = random.randint(1, 20)

while contador != 5 :
    
    contador += 1

    a = (int(input("ingrese su numero : ")))

    if a > r:
        print("mi numero es menor")

    if a < r:
        print("mi numero es mayor")


    if a == r:
        contador = 5

        print("Adivinaste, mi numero era ", r)

    if (contador == 5) and (a != r):

        print("No adivinaste, mi número era ", r)