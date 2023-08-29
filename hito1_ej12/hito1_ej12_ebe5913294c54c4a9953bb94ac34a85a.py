#Juego adivina mi número
from random import randint

nOculto = randint(1, 20)
intentosMax = 5
while True:
    if intentosMax == 0:
        print("No adivinaste, mi número era", nOculto)
        break
    intento = int(input())
    if intento == nOculto:
        print("Adivinaste, mi número era", nOculto)
        break
    elif intento < nOculto:
        print("mi número es mayor")
        intentosMax -= 1
    elif intento > nOculto:
        print("mi número es menor")
        intentosMax -= 1