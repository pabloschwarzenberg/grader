#Juego adivina mi número
from random import randint
azar = randint(1,20)
intentos = 0

if intentos < 5:
    while intentos < 5:
        numPersona = int(input("Adivina mi número ->"))

        if numPersona == azar:
            print("Adivinaste, mi número era", azar)
            break
        if numPersona > azar:
            print("Mi número es menor")

        if numPersona < azar:
            print("Mi número es mayor")
            
        intentos = intentos + 1
        
        if intentos == 5:
            print("No adivinaste, mi número era", azar)
            break      