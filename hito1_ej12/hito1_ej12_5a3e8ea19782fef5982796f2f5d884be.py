#Juego adivina mi número
import random
numero=random.randint(1,20)
n=int(input("Ingresa un número del 1 al 20:"))
x=0
while x<4:
    if n>numero:
        print("mi número es menor")
        n=int(input("Ingresa un número del 1 al 20:"))
        x=x+1
        if n==numero:
            print("Adivinaste, mi número era:",numero)
            x=6
    if n<numero:
        print("mi número es mayor")
        n=int(input("Ingresa un número del 1 al 20:"))
        x=x+1
        if n==numero:
            print("Adivinaste, mi número era:",numero)
            x=6
if x==4:
    print("No adivinaste, mi número era:",numero)      