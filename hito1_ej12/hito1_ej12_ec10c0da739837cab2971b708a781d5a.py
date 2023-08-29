#Juego adivina mi número
import random

a = random.randint(1,20)

intento = 0

while intento<5:
    num = int(input())
    if 1<num<a:
        print("Mi número es mayor")
        intento+=1
    elif num>a and num<20:
        print("Mi número es menor")
        intento+=1
    elif num<1:
        print("Ese número no está entre 1 y 20")
        intento += 1
    elif num>20:
        print("Ese número no está entre 1 y 20")
        intento += 1
    elif num==a:
        print("Adivinaste, mi número era {}".format(a))
        intento=6

if intento == 5:
    print("No adivinaste, mi número era {}".format(a))

elif intento==6:
    print("Fin")
    print("No adivinaste, mi número era {}".format(a))
