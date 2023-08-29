#Juego adivina mi número
import random
print("Adivina mi numero del 1 al 20.(Tienes 5 intentos): ")
numero=random.randint(1,20)
intentos=0
while intentos<5:
    print("¿Cuál es mi número?: ")
    n1=input()
    n1=int(n1)
    intentos=intentos+1
    if n1<numero:
        print("mi numero es mayor")
    elif n1>numero:
        print("mi numero es menor")
    elif n1==numero:
        break
if n1==numero:
    print("Adivinaste,mi numero era",numero)
if intentos==5 and n1!=numero:
    print("No adivinaste, mi numero era",numero)    