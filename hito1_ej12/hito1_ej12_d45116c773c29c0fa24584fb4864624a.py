#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("He generado un número entre 1 y 20. Tienes 5 intentos para adivinarlo.")

    for i in range(intentos):
        print("\nIntento {}/{}".format(i + 1, intentos))
        adivinanza = int(input("Ingresa tu número: "))

        if adivinanza == numero_secreto:
            print("¡Adivinaste! Mi número era {}".format(numero_secreto))
            return
        elif adivinanza < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

    print("\n¡No adivinaste! Mi número era {}".format(numero_secreto))

adivina_mi_numero()
      