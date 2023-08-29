import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    while intentos > 0:
        numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))

        if numero_ingresado == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

# Llamamos a la función para iniciar el juego
adivina_mi_numero()