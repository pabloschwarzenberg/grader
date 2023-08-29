#Juego adivina mi número
from random import randint
print('Estoy pensando en un numero entre 1 y 20: ')
a = randint(1,20)
intentos = 0
while intentos < 5:
    adivina = int(input('Adivina el numero: '))
    intentos += 1
    if adivina < a:
        print('Mi numero es mayor')
    if adivina > a:
        print('Mi numero es menor')
    if adivina == a:
       break
if adivina == a:
    print('Adivinaste, mi numero era ' + str(a))
if adivina != a:
    print('No adivinaste, mi numero era ' + str(a))      