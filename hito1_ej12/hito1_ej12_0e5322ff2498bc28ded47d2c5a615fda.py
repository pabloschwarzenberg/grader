#Juego adivina mi número
import random

intentos=0

numero=random.randint(1, 2)

while intentos < 5:
    x=int(input("Numero:"))

    intentos=intentos + 1

    if (x < numero):
        print("el numero ingresado es menor")
    else:
        if (x > numero):
            print("el numero ingresado es mayor")
        else:
            if (x==numero):
                break

if (x==numero):
    numero=str(numero)
    print("Adivinaste, mi número era"," " + numero)
else:
    numero=str(numero)
    print("No adivinaste, mi numero era"," " + numero)      