#Juego adivina mi número
import random

numero=random.randrange(1,20)
intentos = 5

while intentos>0:

    adivina = int(input("Adivina, ingresa el número de 1 a 20: "))
    if adivina==numero:
        intentos=-1
        print("Adivinaste, mi número era "+str(numero))
    else:
        if adivina<numero:
            print("mi número es mayor")
        else:
            print("mi número es menor")
        intentos -= 1

if intentos==0:
    print("No adivinaste, mi número era "+str(numero))
      