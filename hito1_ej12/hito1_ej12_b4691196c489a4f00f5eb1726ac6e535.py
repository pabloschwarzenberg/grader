#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Estoy pensando en un número entre 1 y 20.")
    print("Tienes 5 intentos para adivinarlo. ¡Buena suerte!")

    while intentos > 0:
        print("\nIntento restante:", intentos)
        numero_adivinar = int(input("Ingresa tu número: "))

        if numero_adivinar == numero_secreto:
            print("Adivinaste, mi número era", numero_secreto)
            return
        elif numero_adivinar < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("\nNo adivinaste, mi número era", numero_secreto)

adivina_mi_numero()
