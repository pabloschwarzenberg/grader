import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a 'Adivina mi número'!")
    print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

    while intentos > 0:
        print("Intento {}/5:".format(6 - intentos))
        intento = int(input("Ingresa un número: "))

        if intento == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if intento < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)

# Ejecutar el juego
adivina_mi_numero()
