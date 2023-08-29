#Juego adivina mi número
import random 
def adivina_mi_numero():
    numero_secreto = random.randint(1, 20)
    intentos = 5

    for i in range(1, intentos + 1):
        print("Intento {}/{}".format(i, intentos))
        numero_ingresado = int(input("Ingresa un número entre 1 y 20: "))

        if numero_ingresado < numero_secreto:
            print("Mi número es mayor.")
        elif numero_ingresado > numero_secreto:
            print("Mi número es menor.")
        else:
            print("¡Adivinaste! Mi número era {}".format(numero_secreto))
            return

    print("No adivinaste. Mi número era {}".format(numero_secreto))

adivina_mi_numero()