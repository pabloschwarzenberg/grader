#Juego adivina mi número
from random import randint
numeroS = randint(1,20)
contador = 0
print(numeroS)
while contador < 5:
    numeroU = int(input("Ingresa tu número: "))
    if numeroU == numeroS:
        print("Adivinaste, mi número era",numeroS)
        contador = 8
    contador+=1
    if contador == 5:
        print("No adivinaste, mi número era",numeroS)
    if (numeroU < numeroS) and contador != 5:
        print("mi número es mayor")
    if (numeroU > numeroS) and contador != 5:
        print("mi número es menor")

      