import random

def guess_my_number():
    secret_number = random.randint(1, 20)
    attempts = 5

    print("¡Bienvenido a 'Adivina mi número'!")
    print("Estoy pensando en un número del 1 al 20.")
    print("Tienes 5 intentos para adivinarlo. ¡Buena suerte!")

    while attempts > 0:
        guess = int(input("Ingresa tu número: "))

        if guess < secret_number:
            print("Mi número es mayor.")
        elif guess > secret_number:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! ¡Mi número era", secret_number, "!")
            return

        attempts -= 1
        print("Te quedan", attempts, "intentos.\n")

    print("¡No adivinaste! Mi número era", secret_number)

guess_my_number()
