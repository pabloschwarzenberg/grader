#Juego adivina mi número
import random

n=random.randint(10,20)
m=6
l=1
q=int(input("Ingrese su numero:"))

while (q!=n) and (m>1):
    if(q>n):
        print("Ingrese un numero menor:")
    elif(q<n):
        print("Ingrese un numero mayor:")
    m=m-1
    l=l+1
    print("Le quedan", m,"intentos")
q=int(input("Ingrese su numero:"))

if(q==n):
    print("Has adivinado,el numero era: ",n)
else:
    print("No has adivinado,el numero era: ",n)      