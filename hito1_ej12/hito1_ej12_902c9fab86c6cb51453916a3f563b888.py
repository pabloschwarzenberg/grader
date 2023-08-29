import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto (entre 1 y 20). ¡Buena suerte!")

    while intentos > 0:
        try:
            guess = int(input("Ingresa tu número: "))
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")
            continue

        if guess < 1 or guess > 20:
            print("El número debe estar en el rango de 1 a 20.")
            continue

        if guess == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if guess < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

# Ejecutar el juego
adivina_mi_numero()
      