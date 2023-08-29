import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("Bienvenido(a) al juego 'Adivina mi número'!")
    print("Tienes que adivinar un número entre 1 y 20.")
    print("Tienes 5 intentos.")

    for i in range(intentos):
        intento = int(input("Ingresa tu número: "))

        if intento == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        elif intento < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

    print("No adivinaste. Mi número era", numero_secreto)

# Ejecutar el juego "Adivina mi número"
adivina_mi_numero()

      