#Juego adivina mi número

import random

intentos_realizados = 0

numero_secreto = random.randint(1, 20)
print ("Adivinar un numero entre 1 y 20: ")

while intentos_realizados <5:
    print ("Intenta adivinar: ")
    estimacion1 = input ()
    estimacion1 = int(estimacion1)

    intentos_realizados = intentos_realizados + 1

    if estimacion1 > numero_secreto:
        print ("mi numero es mayor")

    if estimacion1 < numero_secreto:
        print ("mi numero es menor")

    if estimacion1 == numero_secreto:
        break

if estimacion1 == numero_secreto:
    intentos_realizados = str(intentos_realizados)
    print ("Adivinaste, mi numero era: ")

if estimacion1 != numero_secreto:
    numero_secreto = str (numero_secreto)
    print ("No adivinaste, mi numero era: ")