#Juego adivina mi número
import random

intentos = 1
numerox = random.randint(1, 20)

while intentos != 6:
    intento = int(input("ingrese numero a adivinar: "))

    intentos += 1
    if intento == numerox:
        break
    if intento < numerox:
        print("mi numero es mayor")
    if intento > numerox:
        print("mi numero es menor")
    
if intento == numerox:
    print("Adivinaste, mi numero era: ", numerox)
if intento != numerox:
    print("No adivinaste, mi numero era: ", numerox)
      