#Juego adivina mi número
import random

numero = random.randint(1, 20)
intento = 1

while intento < 6:
    aleatorio = int(input('Adivina el número entre 1 y 20: '))
    if aleatorio < numero:
        print('Mi número es mayor')
        intento += 1
    elif aleatorio > numero:
        print('Mi número es menor')
        intento += 1
    else:
        print("Adivinaste, mi número era: ",numero)
        break
else:
    print("No adivinaste, mi número era: ",numero)