import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido a Adivina mi número!")
    print("Estoy pensando en un número del 1 al 20.")
    print("Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        try:
            adivinanza = int(input("Ingresa tu número: "))
        except ValueError:
            print("¡Debes ingresar un número!")
            continue

        if adivinanza < numero_secreto:
            print("Mi número es mayor.")
        elif adivinanza > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

# Ejemplo de uso
adivina_mi_numero()