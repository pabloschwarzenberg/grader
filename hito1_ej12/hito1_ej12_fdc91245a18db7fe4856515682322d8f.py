#Juego adivina mi número
import random

def adivinar():
    numero_s = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a 'Adivina mi número'!")
    print("He elegido un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        numero_i = int(input("Ingresa tu número: "))

        if numero_i == numero_s:
            print("¡Adivinaste! Mi número era", numero_s)
            return

        if numero_i < numero_s:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_s)

adivinar()      