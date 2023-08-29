#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido al juego Adivina mi número!")
    print("Estoy pensando en un número del 1 al 20.")
    print("Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        print("Intento:", 6 - intentos)
        numero_ingresado = int(input("Ingresa un número: "))

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")
        elif numero_ingresado > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste, mi número era", numero_secreto, "!")
            return

        intentos -= 1

    print("No adivinaste, mi número era", numero_secreto)

# Ejecutar el juego
adivina_mi_numero()
      