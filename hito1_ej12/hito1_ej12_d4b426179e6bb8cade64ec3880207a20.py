import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto (entre 1 y 20).")

    while intentos > 0:
        print("Intentos restantes:", intentos)
        guess = int(input("Ingresa tu número: "))

        if guess == numero_secreto:
            print("Adivinaste, mi número era", numero_secreto)
            return
        elif guess < numero_secreto:
            print("Mi número es mayor")
        else:
            print("Mi número es menor")

        intentos -= 1

    print("No adivinaste, mi número era", numero_secreto)


adivina_mi_numero()
      