#Juego adivina mi número
import random

numero = 0
secreto = random.randint(1,20)
intento = 0

while numero != secreto and intento<5:
    numero = int(input("Ingrese un numero: "))
    intento += 1
    if numero >secreto:
        print("Mi numero es menor")
    else:
        print("Mi numero es mayor")
if numero == secreto:
    print("Adivinaste, mi numero era:",secreto)
else:
    print("No adivinaste, mi numero era:",secreto)    