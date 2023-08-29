#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido al juego Adivina mi número. Estoy pensando en un número del 1 al 20.")
    print("Tienes 5 intentos para adivinarlo. ¡Buena suerte!")

    while intentos > 0:
        print("Intento:", 6 - intentos)
        guess = int(input("Ingresa tu número: "))

        if guess < numero_secreto:
            print("Mi número es mayor.")
        elif guess > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()     