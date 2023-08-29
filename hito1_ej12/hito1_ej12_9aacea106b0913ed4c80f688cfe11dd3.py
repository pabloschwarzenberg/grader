#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto, el cual está entre 1 y 20.")

    for i in range(1, intentos + 1):
        print(f"\nIntento {i}:")
        numero_ingresado = int(input("Ingresa tu número: "))

        if numero_ingresado == numero_secreto:
            print(f"Adivinaste, ¡mi número era {numero_secreto}!")
            return

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")

        if numero_ingresado > numero_secreto:
            print("Mi número es menor.")

    print(f"\nNo adivinaste, ¡mi número era {numero_secreto}!")

adivina_mi_numero()      