import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Estoy pensando en un número entre 1 y 20.")

    while intentos > 0:
        print("Tienes", intentos, "intentos restantes.")

        try:
            numero = int(input("Ingresa tu número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if numero < numero_secreto:
            print("Mi número es mayor.")
        elif numero > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
