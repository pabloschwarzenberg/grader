#Juego adivina mi número
      
import random

def generar_numero_secreto():
    return random.randint(1, 20)

def adivina_mi_numero():
    numero_secreto = generar_numero_secreto()
    intentos = 5

    print("¡Bienvenido al juego Adivina mi número!")
    print("Tienes 5 intentos para adivinar el número secreto.")

    for i in range(intentos):
        numero_ingresado = int(input("Intento {}: Ingresa un número entre 1 y 20: ".format(i + 1)))

        if numero_ingresado == numero_secreto:
            print("¡Adivinaste! Mi número era", numero_secreto)
            return
        elif numero_ingresado < numero_secreto:
            print("Mi número es mayor.")
        else:
            print("Mi número es menor.")

    print("No adivinaste. Mi número era", numero_secreto)

adivina_mi_numero()
