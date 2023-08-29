import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    for i in range(intentos):
        print("Intento", i + 1)
        numero = int(input("Ingresa un número entre 1 y 20: "))

        if numero == numero_secreto:
            print("Adivinaste, mi número era", numero_secreto)
            return
        elif numero < numero_secreto:
            print("Mi número es mayor")
        else:
            print("Mi número es menor")

    print("No adivinaste, mi número era", numero_secreto)

# Ejecutar el juego
adivina_mi_numero()