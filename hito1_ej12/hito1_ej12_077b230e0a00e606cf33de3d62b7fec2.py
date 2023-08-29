#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    while intentos > 0:
        numero = int(input("Ingresa un número entre 1 y 20: "))

        if numero == numero_secreto:
            print("Adivinaste, mi número era", numero_secreto)
            return

        if numero < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1

    print("No adivinaste, mi número era", numero_secreto)


adivina_mi_numero()
      