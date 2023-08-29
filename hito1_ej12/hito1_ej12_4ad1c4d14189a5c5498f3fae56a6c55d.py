#Juego adivina mi número
import random
print('** ADIVINA MI NÚMERO **')

numero_secreto = random.randint(1,20)
cont = 0
while cont < 5:
    numero = int(input('Ingrese el número: '))
    if numero < numero_secreto:
        print('Tu número es menor que el número secreto')
        cont = cont + 1
    elif numero > numero_secreto:
        print('Tu número es mayor que el número secreto')
        cont = cont + 1
    elif numero == numero_secreto:
        print('Adivinaste, mi número era '+str(numero_secreto))
        break
    
if cont == 5:
    print('No adivinaste, mi número era '+str(numero_secreto))      