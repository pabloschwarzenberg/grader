#Juego adivina mi número
from random import *

numero = randint(1, 20)
print(numero)
i = 0
adivinar = 0

while (adivinar != numero):
    adivinar = int(input('Adivina el numero: '))
    if adivinar > numero:
        print("mi numero es menor")
        i = i + 1
    if adivinar < numero:
        print("mi numero es mayor")
        i = i + 1
    if i == 5:
        break

if (i == 5) and (adivinar == numero):
    print("Adivinaste, mi número era", numero)
elif i == 5:
    print("No adivinaste, mi número era", numero)
elif adivinar == numero:
    print("Adivinaste, mi número era", numero)   