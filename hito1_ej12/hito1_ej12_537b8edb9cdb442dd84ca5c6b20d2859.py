import random

n=random.randint(1,20)
print(n)
intentos=5
while intentos!=0:
    n2=int(input("Ingrese numero :"))
    if n2==n:
        print("Adivinaste, mi numero era ",n)
        break
    elif n>n2:
        print("El numero es mayor que eso")
        intentos=intentos-1
    elif n<n2:
        print("El numero es menor que eso")
        intentos=intentos-1
if intentos==0:
    print("No adivinaste, mi numero era ",n)