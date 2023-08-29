#Juego adivina mi número
import random

Intentoshechos = 0
Numerominimo = 1
Numeromaximo = 20

print("Hi! cual es tu nombre?: ")
nombre = input()

numero = (random.randint(Numerominimo, Numeromaximo))

print("Lo recordare, " + ' puedes adivinar mi numero secreto? ¡Pista! se encuentra entre ' + str(Numerominimo) + ' y ' + str(Numeromaximo))

while Intentoshechos < 5:
    print("adivina: ")
    Intento = input()
    Intento = int(Intento)

    Intentoshechos = Intentoshechos + 1

    if Intento < numero:
        print("mi número es mayor. ")
    if Intento > numero:
        print("mi número es menor. ")
    if Intento == numero:
        break

if Intento == numero:
        numero = str(numero)
        print("Adivinaste, mi numero era " + numero)

if Intento != numero:
        numero = str(numero)
         
        print("No adivinaste, mi numero era " + numero)      