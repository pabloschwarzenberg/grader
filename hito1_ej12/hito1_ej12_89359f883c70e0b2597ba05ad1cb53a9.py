import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido a Adivina mi número!")
    print("Estoy pensando en un número entre 1 y 20.")
    print("Tienes 5 intentos para adivinar el número.")

    while intentos > 0:
        print("Intento:", 6 - intentos)
        guess = int(input("Ingresa tu número: "))

        if guess == numero_secreto:
            print("Adivinaste, mi número era", numero_secreto)
            return

        if guess < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste, mi número era", numero_secreto)

adivina_mi_numero()
     