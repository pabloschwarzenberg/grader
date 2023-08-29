import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Estoy pensando en un número del 1 al 20. ¡Adivina cuál es!")

    while intentos > 0:
        intento = int(input("Ingresa tu intento: "))

        if intento < numero_secreto:
            print("Mi número es mayor.")
        elif intento > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()