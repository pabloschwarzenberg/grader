#clase 7
from random import randint
n=randint(1,20)
cont=5
for i in range(5):
    ingresado=int(input("Ingrese su opcion "+str(i+1)+":"))
    if n==ingresado:
        print("Adivinaste, mi número era "+str(n))
        break
    elif ingresado<n:
        print("Mi numero es mayor")
    elif ingresado>n:
        print("Mi numero es menor")
    if i ==4:
        print("No adivinaste, mi número era "+str(n))

