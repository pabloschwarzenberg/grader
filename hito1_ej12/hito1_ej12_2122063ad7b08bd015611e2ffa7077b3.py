#Juego adivina mi número
import random

def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 0

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto.")

    while intentos < 5:
        intentos += 1
        numero = int(input("Intento #" + str(intentos) + ": Ingresa un número del 1 al 20: "))

        if numero == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        elif numero < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

    print("No adivinaste. Mi número era", numero_secreto)


adivina_mi_numero()
     