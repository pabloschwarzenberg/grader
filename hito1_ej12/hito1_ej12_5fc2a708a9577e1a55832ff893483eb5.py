from random import randint
n=(randint(1,20))
c=0
while True:
    numero=int(input("Ingrese numero: "))
    if numero==n:
        print("Adivinaste, mi numero era",n)
        break
    elif numero<n:
        print("el numero es mayor")
    elif numero>n:
        print("el numero es menor")
    c=c+1
    if c==5:
        print("No adivinaste, mi numero era",n)
        break