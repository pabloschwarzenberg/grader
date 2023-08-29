import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto.")

    while intentos > 0:
        print(f"Intento {6 - intentos}:")
        numero = int(input("Ingresa un número del 1 al 20: "))

        if numero == numero_secreto:
            print("¡Adivinaste!")
            print(f"Mi número era {numero_secreto}")
            return

        elif numero < numero_secreto:
            print("Mi número es mayor.")

        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste.")
    print(f"Mi número era {numero_secreto}")

adivina_mi_numero()
