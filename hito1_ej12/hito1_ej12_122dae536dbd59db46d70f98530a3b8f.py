#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 0

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar un número entre 1 y 20.")

    while intentos < 5:
        intentos += 1
        numero_ingresado = int(input("Intento {}: Ingresa un número: ".format(intentos)))

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")
        elif numero_ingresado > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Felicidades! Adivinaste mi número en {} intentos.".format(intentos))
            return

    print("¡Lo siento! No lograste adivinar mi número. Era el número {}.".format(numero_secreto))

adivina_mi_numero()
      