#Juego adivina mi número

import random

i=0
computador = random.randrange(1,20)
while True:
    jugador = int(input())
    if jugador == computador:
        print("Adivinaste, mi número era", computador)
    elif jugador < computador:
        print("el numero que escogí es mayor al que ingresaste")
    elif jugador > computador:
        print("el numero que escogí es menor al que ingresaste")
    i+=1
    if i == 5:
        break
print("No adivinaste, mi número era", computador)