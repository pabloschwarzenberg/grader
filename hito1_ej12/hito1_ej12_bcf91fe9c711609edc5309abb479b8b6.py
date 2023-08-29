#Juego adivina mi número
import random
intentos = 0
Numerominimo = 1
Numeromaximo = 20
num = random.randint(Numerominimo, Numeromaximo)
print("Adivina el numero secreto entre 1-20")
while intentos < 5:
    adivinar = input("ingresa el numero: ")
    adivinar = int(adivinar)
    intentos = intentos + 1
    if adivinar < num:
        print("mi numero es mayor")
    if adivinar > num:
        print("mi numero es menor")
    if adivinar == num:
        break

if adivinar == num:
    print("Adivinaste, mi número era " + str(num))
if adivinar != num:
    print("No adivinaste, mi número era " + str(num))      