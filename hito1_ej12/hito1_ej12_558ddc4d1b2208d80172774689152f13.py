#Juego adivina mi número
import random
a=random.randint(1,20)
b=0
m=False
while b<5:
    c=int(input("ingrese un número:"))
    if c==a:
        print("Adivinaste, mi número era",a)
        break
    if c<a:
        print("El número ingresado es menor")
    if c>a:
        print("El número ingresado es mayor")
    b=b+1

if b==5:
    print("No adivinaste, mi número era",a)     


      