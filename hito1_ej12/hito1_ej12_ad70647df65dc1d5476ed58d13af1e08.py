from random import randint
from time import sleep

def adivina_mi_numero():
    secreto = randint(1, 20)

    for intento in range(1, 6):
        numero = int(input("Ingrese un número: "))

        if numero == secreto:
            sleep(1)
            print("¡Adivinaste! Mi número era", secreto)
            return True

        elif numero > secreto:
            print("Mi número es menor.")
        else:
            print("Mi número es mayor.")

        print("Intento N°", intento)
        sleep(1)

    print("No adivinaste en 5 intentos. Mi número era", secreto)
    return False

adivina_mi_numero()
