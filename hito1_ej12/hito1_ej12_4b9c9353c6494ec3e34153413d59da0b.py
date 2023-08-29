import random
x=random.randint(1, 20)
intento=0
while True:
    intento=intento+1
    i=eval(input("Adivina el numero: "))
    if i>x:
        print("Tu numero es mayor al incognito")
    elif i<x:
        print("Tu numero es menor al incognito")
    else:
        print("Adivinaste, mi número era",x)
        break
    if intento==5:
        print("No adivinaste, mi número era",x)
        break
