#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("He elegido un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

    for i in range(intentos):
        print("\nIntento", i + 1)
        intento = int(input("Ingresa tu número: "))

        if intento < numero_secreto:
            print("Mi número es mayor.")
        elif intento > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return

    print("\nNo adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
     