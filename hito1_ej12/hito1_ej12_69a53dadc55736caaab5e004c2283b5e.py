#Juego adivina mi número
import random

intentos = 0
numero = random.randint(0, 20)
print(numero)

while intentos < 5:
    adivina = int(input('Ingrese un numero entre 0 y 20: '))
    intentos = intentos + 1

    print(adivina)
    print(intentos)

    if adivina < numero:
        print('¡Mi numero es mayor!')
    if adivina > numero:
        print('¡Mi numero es menor!')
    if adivina == numero:
        break

if adivina == numero:
    print("Adivinaste, mi número era {}".format(numero))
if adivina != numero:
    print("No adivinaste, mi número era {}".format(numero))