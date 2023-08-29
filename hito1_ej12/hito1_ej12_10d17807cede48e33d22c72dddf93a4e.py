import random

intentos = 0

print('Dime tu nombre?')
nombre = input()

numero = random.randint(1, 20)
print('Bueno, ' + nombre + ', piensa en un numero entre 1 y 20')

while intentos < 5:
    print('adivinalo tienes cinco intentos')
    adivina = input()
    adivina = int(adivina)

    intentos = intentos + 1

    if adivina < numero:
        print('mi numero es mayor')

    if adivina > numero:
        print('mi numero es menor')

    if adivina == numero:
        break

if adivina == numero:
    intentos = str(intentos)
    print('adivinaste, ' + nombre + '! mi numero era ' + intentos)

if adivina != numero:
    numero = str(numero)
    print('no adivinaste, mi numero era ' + numero)