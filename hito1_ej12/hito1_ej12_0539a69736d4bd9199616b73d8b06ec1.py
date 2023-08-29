#Juego adivina mi número
import random
from random import randint

num1=randint(1,20)
intento=1
while True:
    if intento==5:
        a=int(input("numero: "))
        if a==num1:
            print("Adivinaste, mi número era",num1)
            break
        print("No adivinaste, mi número era ",num1)
        break
    if intento<5:
        a=int(input("numero: "))
        if a>num1:
            print("mi número es menor")
        if a<num1:
            print("mi número es mayor")
        if a==num1:
            print("Adivinaste, mi número era",num1)
            break
        else:
            intento=intento+1     