#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a Adivina mi número!")
    print("Estoy pensando en un número entre 1 y 20.")
    print("Tienes 5 intentos para adivinarlo. ¡Buena suerte!")

    while intentos > 0:
        print("Intento:", 6 - intentos)
        numero_ingresado = int(input("Ingresa un número: "))

        if numero_ingresado == numero_secreto:
            print("¡Adivinaste! ¡Mi número era", numero_secreto, "!")
            return

        elif numero_ingresado < numero_secreto:
            print("Mi número es mayor.")

        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste. ¡Mi número era", numero_secreto, "!")

# Llamamos a la función principal para comenzar el juego
adivina_mi_numero()
