#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    while intentos > 0:
        print("Tienes", intentos, "intentos restantes.")
        numero = int(input("Adivina el número (entre 1 y 20): "))

        if numero == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        elif numero < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste. Mi número era", numero_secreto)


adivina_mi_numero()
      