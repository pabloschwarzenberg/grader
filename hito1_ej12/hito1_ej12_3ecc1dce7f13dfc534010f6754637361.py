#Juego adivina mi número
import random
numero=random.randint(1, 20)
intentos=0
while intentos<5:
    juego=int(input('Ingrese numero'))
    if juego<numero:
        print('mi número es mayor')
    if juego>numero:
        print('mi número es menor')
    if juego==numero:
        print('Adivinaste, mi número era ',numero)
        break
    intentos += 1
    if intentos==5:
        print('No adivinaste, mi número era ',numero)      