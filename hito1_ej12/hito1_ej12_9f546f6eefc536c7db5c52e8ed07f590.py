import random

def adivina_mi_numero_secreto():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego de adivina mi número!")
    print("Tienes solamente 5 intentos para adivinar mi numero")
    print("Estoy pensando en un numero entre 1 y 20.")
    print("Tienes 5 intentos para adivinarlo. ¡Buena suerte!")

    while intentos > 0:
        intento = int(input("Ingresa tu número: "))

        if intento == numero_secreto:
            print("¡Adivinaste!¡FELICITACIONES! Mi número era", numero_secreto)
            return
        elif intento < numero_secreto:
            print("Mi número es mayor.\n")
        else:
            print("Mi número es menor.\n")

        intentos -= 1
        print("Te quedan", intentos, "intentos.\n")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero_secreto()