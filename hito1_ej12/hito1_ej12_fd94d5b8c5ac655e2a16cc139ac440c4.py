import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto (entre 1 y 20). ¡Buena suerte!\n")

    while intentos > 0:
        guess = int(input("Ingresa tu número: "))

        if guess == numero_secreto:
            print("¡Adivinaste! ¡Mi número era", numero_secreto, "!")
            return

        if guess < numero_secreto:
            print("Mi número es mayor. Intenta de nuevo.\n")
        else:
            print("Mi número es menor. Intenta de nuevo.\n")

        intentos -= 1

    print("¡No adivinaste! Mi número era", numero_secreto)

adivina_mi_numero()

      