#Juego adivina mi número
#adivina el numero secreto

import random
numero = random.randint(1, 20)
intentos = 0
while intentos<5:
    j=int(input("Ingrese un numero :"))
    if j<numero:
        print("mi número es mayor")
    if j>numero:
        print("mi número es menor")
    if j==numero:
        print("Adivinaste, mi número era ",numero)
        break
    intentos += 1
    if intentos==5:
        print("No adivinaste, mi número era ",numero)