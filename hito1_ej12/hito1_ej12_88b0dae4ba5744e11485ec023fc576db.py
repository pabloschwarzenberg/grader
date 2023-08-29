#Juego adivina mi número
import random

numero = random.randint(1, 20)
intentos = 5
flag = False
while intentos != 0:
    eleccion = int(input("Elige un numero: "))
    if eleccion > numero:
        print("mi número es menor")
        intentos -= 1
    elif eleccion < numero:
        print("mi número es mayor")
        intentos -= 1

    elif eleccion == numero:
        print("Adivinaste, mi número era {}".format(numero))
        flag = True
        break
if not flag:
    print("No adivinaste, mi número era {}".format(numero))
