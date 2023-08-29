#Juego adivina mi número
print("adivina mi número")
intentos=5
import random
n=random.randint(1,20)
while intentos>=1:
    x=int(input("ingrese un numero:"))
    if n>x:
        print("el número que escogiste es menor")
        intentos=intentos-1
    elif n<x:
        print("el número que escogiste es mayor")
        intentos=intentos-1
    elif n==x:
        print("adivinaste mi número, mi numero era:",n)
else:
        print("no adivinaste, mi numero era:",n)     
   
   