#Juego adivina mi número
from random import randint

numeroRandom = randint(1,20)

i = 0
while i < 5:
    num = int(input("Ingrese intento: "))
    if i == 4:
        print("No adivinaste, mi número era ", numeroRandom)
        break
    if num == numeroRandom:
        print("Adivinaste")
    elif num < numeroRandom:
        print("mi número es mayor")
    else:
        print("mi número es menor")

    i += 1
      