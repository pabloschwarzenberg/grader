#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a 'Adivina mi número'!")
    print("Estoy pensando en un número entre 1 y 20.")

    while intentos > 0:
        print(f"\nTienes {intentos} intentos restantes.")
        try:
            guess = int(input("Ingresa tu número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if guess < numero_secreto:
            print("Mi número es mayor.")
        elif guess > numero_secreto:
            print("Mi número es menor.")
        else:
            print(f"\n¡Adivinaste! Mi número era {numero_secreto}.")
            return

        intentos -= 1

    print(f"\n¡No adivinaste! Mi número era {numero_secreto}.")

adivina_mi_numero()