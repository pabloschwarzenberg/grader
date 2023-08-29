#Juego adivina mi número
from random import randint
numero=randint(1,20)
intentos=0

while intentos<5:
    usuario=int(input("Ingrese el número:"))
    intentos+=1
    if usuario!=numero:
        if usuario<numero:
            print("mi número es mayor")
        if usuario>numero:
            print("mi número es menor")
        if intentos==5:
         print("No adivinaste,mi número era", numero)   
    if usuario==numero:
        print("Adivinaste,mi número era",numero)
        break      