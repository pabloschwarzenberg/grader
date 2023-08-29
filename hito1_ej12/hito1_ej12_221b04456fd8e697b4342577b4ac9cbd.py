#Juego adivina mi número
achunte=int(input("tirate un numerazo del 1 al 20"))
import random
x=random.randint(0,20)
f=0

while achunte!=x:
    if achunte>x:
        print("el numero es menor")
    if achunte<x:
        print("el numero es mayor")
    f=f+1
    if f==5:
        print("No adivinaste, mi numero era",x)
        break
    achunte=int(input("tirate otro po"))

if achunte==x:
    print("Adivinaste, mi numero era ",x)
