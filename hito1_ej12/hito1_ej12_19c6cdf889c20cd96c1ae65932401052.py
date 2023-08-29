#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

    while intentos > 0:
        print("Intentos restantes:", intentos)
        intento = int(input("Ingresa tu número: "))

        if intento == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if intento < numero_secreto:
            print("Mi número es mayor")
        else:
            print("Mi número es menor")

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()

#FIN
      