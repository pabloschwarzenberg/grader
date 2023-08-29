import random

def generar_numero_secreto():
    return random.randint(1, 20)

def adivina_mi_numero():
    numero_secreto = generar_numero_secreto()
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto (entre 1 y 20). ¡Buena suerte!")

    while intentos > 0:
        intento = int(input("Ingresa tu número: "))

        if intento == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if intento < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("¡No adivinaste! Mi número era", numero_secreto)

adivina_mi_numero()
