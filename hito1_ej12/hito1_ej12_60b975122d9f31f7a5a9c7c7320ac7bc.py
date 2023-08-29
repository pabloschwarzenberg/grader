#Juego adivina mi número
import random

intento = 0

numero_secreto = random.randint(1, 20)
print(numero_secreto)
numero_usuario = input("Ingrese numero entre el 1 y 20:")
numero_usuario = int(numero_usuario)

while intento < 6:

    #numero_usuario = input("Ingrese numero entre el 1 y 20:")
    #numero_usuario = int(numero_usuario)

    intento = intento + 1

    if numero_usuario < numero_secreto:
        print("mi numero es menor")

    if numero_usuario > numero_secreto:
        print("mi numero es mayor")

    if numero_usuario == numero_secreto:
        break

if numero_usuario == numero_secreto:
    print("Adivinaste, mi número era",numero_secreto)

if numero_usuario != numero_secreto:
    print("No adivinaste, mi número era",numero_secreto)     