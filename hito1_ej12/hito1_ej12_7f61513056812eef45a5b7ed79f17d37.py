#Juego adivina mi número
import random
x=random.randint(1,20)
a=int(input("Ingrese intento 1: "))
if a==x :
    print("Adivinaste, mi numero era ",x," ")
    quit()
elif a<x :
    print("No adivinasta, el numero es mayor")
elif a>x :
    print("No adivinaste, el numero es menor")
    
b=int(input("Ingrese intento 2: "))
if b==x :
     print("Adivinaste, mi numero era ",x," ")
     quit()
elif b<x :
     print("No adivinaste, el numero es mayor")
elif b>x :
     print("No adivinaste, el numero es menor")
            
c=int(input("Ingrese intento 3: "))
if c==x :
    print("Adivinaste, mi numero era ",x," ")
    quit()
elif c<x :
    print("No adivinaste, el numero es mayor")
elif c>x :
    print("No adivinaste, el numero es menor")

d=int(input("Ingrese intento 4: "))
if d==x :
    print("Adivinaste, mi numero era ",x," ")
    quit()
elif d<x :
    print("No adivinaste, el numero es mayor")
elif d>x :
    print("No adivinaste, el numero es menor")

e=int(input("Ingrese intento 5: "))
if e==x :
    print("Adivinaste, mi numero era ",x," ")
    quit() 
else:
    print("No adivinaste, mi numero era ",x," ")