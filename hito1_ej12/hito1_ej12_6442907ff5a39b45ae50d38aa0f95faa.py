import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto, que está entre 1 y 20.")

    for i in range(intentos):
        print("Intento", i+1)
        guess = int(input("Ingresa un número: "))

        if guess < numero_secreto:
            print("Mi número es mayor.")
        elif guess > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
      