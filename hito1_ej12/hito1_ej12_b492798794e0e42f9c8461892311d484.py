#Juego adivina mi número
import random

intentos = 0
numerosecreto = random.randint(1, 20)
while intentos != 5:
    numeroescogido = int(input("ingrese un numero entre 0 y 20: "))
    if numeroescogido == numerosecreto:
        print("Adivinaste, mi número era {}".format(numerosecreto))
        break
    elif numeroescogido > numerosecreto:
        print("mi número es menor")
        intentos += 1
    else:
         print("mi número es mayor")
         intentos += 1
if intentos == 0:
    print("No adivinaste, mi número era {}".format(numerosecreto))      