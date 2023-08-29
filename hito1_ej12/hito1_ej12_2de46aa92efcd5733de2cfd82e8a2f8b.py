import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    while intentos > 0:
        print("Intentos restantes:", intentos)
        adivinanza = int(input("Adivina el número (entre 1 y 20): "))

        if adivinanza == numero_secreto:
            print("¡Adivinaste, mi número era", numero_secreto, "!")
            return

        if adivinanza < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste, mi número era", numero_secreto, ".")

adivina_mi_numero()
