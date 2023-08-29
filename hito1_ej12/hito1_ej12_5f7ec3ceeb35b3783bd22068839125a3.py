#Juego adivina mi número
import random
x = random.randint(1,20)
intentos = 0
sw = True
while sw:
    numero = int(input('Ingrese un numero: '))
    intentos += 1
    if numero == x:
        print("Adivinaste, mi número era",x)
        sw = False
    elif intentos == 5:
        print("No adivinaste, mi número era",x)
        sw = False
    elif numero > x:
        print('mi número es menor')
    else:
        print('mi número es mayor')