#Juego adivina mi número
import random
x= random.randint(1,20)
y=int(input("ingresa un numero:"))
intentos=5
if x==y:
    print("adivinaste, mi numero era",x)
else:
    while x!=y and intentos>0:
         if y<x:
            print("mi numero es mayor")
         if y>x:
            print("mi numero es menor")
         y=int(input("ingresa un numero:"))
         intentos=intentos-1
         if x==y:
             print("adivinaste, mi numero era",x)
        