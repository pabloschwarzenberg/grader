import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Estoy pensando en un número del 1 al 20.")
    print("Tienes 5 intentos para adivinarlo. ¡Buena suerte!")

    while intentos > 0:
        print("Intentos restantes:", intentos)
        numero_ingresado = int(input("Ingresa un número: "))

        if numero_ingresado == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")

        if numero_ingresado > numero_secreto:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
