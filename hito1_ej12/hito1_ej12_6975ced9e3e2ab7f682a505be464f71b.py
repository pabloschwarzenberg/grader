#Juego adivina mi número
import random
intentos=5
n=random.randint(1,20)
while intentos>0:
    a=int(input("adivina el numero:")) 
    if a>n:
        print ("tu numero es mayor")
    elif a<n:
        print("tu numero es menor")
    elif a==n:
        print("Adivinaste, mi número era",a)
    intentos = intentos-1
    if intentos==0:
        print("No adivinaste, mi número era",n)  