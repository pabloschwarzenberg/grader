#Juego adivina mi número
import random
intentos = 0
minNumero = 1
maxNumero = 20

numero = random.randint(minNumero, maxNumero)
print("Adivina el numero secreto entre 1-20")

while intentos < 5:
    adiv = input("ingresa el numero: ")
    adiv = int(adiv)

    intentos = intentos + 1

    if adiv < numero:
        print("mi numero es mayor")
    if adiv > numero:
        print("mi numero es menor")
    if adiv == numero:
        break

if adiv == numero:
    print("Adivinaste, mi número era " + str(numero))
if adiv != numero:
    print("No adivinaste, mi número era " + str(numero))      