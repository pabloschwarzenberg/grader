#Juego adivina mi número
import random
x=random.randint(1,21)


a=5
while a!=0:
    z=int(input())
    if z>x:
       print("el numero ingresado es menor que el numero secreto")
       a=a-1
    elif z<x:
       print("el numero ingresado es mayor que el numero secreto")
       a=a-1
    elif z==x:
       print("Adivinaste, mi numero era "+str(x))
if a==0:
       print("se te acabaron los intentos")
       print("no adivinaste mi numero era"+str(x))
       