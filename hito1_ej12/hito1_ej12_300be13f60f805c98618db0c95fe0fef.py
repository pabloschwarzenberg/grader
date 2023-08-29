import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido a Adivina Mi Número!")
    print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

    while intentos > 0:
        intento = int(input("Ingresa tu número: "))

        if intento < numero_secreto:
            print("Mi número es mayor.")
        elif intento > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
