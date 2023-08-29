#Juego adivina mi número
from random import randint
condicion = True
contador = 0
numero_secreto = randint(1,20)
while condicion:
    a = eval(input('adivina mi numero: '))
    if a == numero_secreto:
        print('Adivinaste, mi número era', numero_secreto)
        break
    if a < numero_secreto:
        print('mi número es mayor')
        contador = contador + 1
    if a > numero_secreto:
        contador = contador + 1
        print('mi número es menor')
    if contador == 5 :
        print('No adivinaste, mi número era', numero_secreto)
        condicion = False
