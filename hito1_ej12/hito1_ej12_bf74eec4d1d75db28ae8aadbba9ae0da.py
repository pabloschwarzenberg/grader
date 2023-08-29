#Juego adivina mi número
#ENTRADA

import random

for i in range(1):
    Num = random.randint(1,20)

contador = 5

Intentos = True

#SALIDA

while Intentos != False and contador >= 0:
    num = int(input("Ingrese un número para adivinar: "))

    if num > Num and contador >= 1:
        if num == Num:
            print("Adivinaste, mi número era " + str(Num))
            Intentos = False
        else:
            print("mi número es menor")
        contador -= 1

    if num < Num and contador >= 1:
        print("mi número es mayor")
        contador -= 1

    if contador == 0:
        print("No adivinaste, mi número era " + str(Num))
        Intentos = False