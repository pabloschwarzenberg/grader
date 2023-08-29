#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    for i in range(intentos):
        numero = int(input("Intento {}: Ingresa un número entre 1 y 20: ".format(i+1)))

        if numero < numero_secreto:
            print("Mi número es mayor.")
        elif numero > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era {}.".format(numero_secreto))
            return

    print("No adivinaste. Mi número era {}.".format(numero_secreto))

# Ejecutar el juego
adivina_mi_numero()
      