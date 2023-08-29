import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a Adivina mi número!")
    print("Estoy pensando en un número entre 1 y 20.")
    print("Tienes 5 intentos para adivinarlo. ¡Buena suerte!")

    while intentos > 0:
        print("Intentos restantes:", intentos)
        guess = int(input("Ingresa tu número: "))

        if guess < numero_secreto:
            print("Mi número es mayor.")
        elif guess > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)


adivina_mi_numero()