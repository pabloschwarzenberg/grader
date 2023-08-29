#Juego adivina mi número
import random
n=(random.randint(1,21))
contador=0
while contador<5:
    intento=int(input("Numero:"))
    if intento==n:
        print("Adivinaste, mi número era",n)
    else:
        if intento>n:
            print("Número ingresado es mayor a número secreto")
            contador+=1
        else:
            contador+=1
            print("Número ingresado es menor a número secreto")
if contador==5:
    print("No adivinaste, mi número era ",n)