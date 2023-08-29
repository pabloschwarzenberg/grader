#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido al juego Adivina mi número.")
    print("Tienes 5 intentos para adivinar el número secreto.")

    for i in range(intentos):
        intento = int(input("Intento {}: Ingresa un número entre 1 y 20: ".format(i + 1)))

        if intento == numero_secreto:
            print("¡Adivinaste! Mi número era {}.".format(numero_secreto))
            return
        elif intento < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

    print("No adivinaste. Mi número era {}.".format(numero_secreto))

adivina_mi_numero()