import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego 'Adivina mi número'!")
    print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        try:
            numero_ingresado = int(input("Ingresa un número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if numero_ingresado == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")

        if numero_ingresado > numero_secreto:
            print("Mi número es menor.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()

      