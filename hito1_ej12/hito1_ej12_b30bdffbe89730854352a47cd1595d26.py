#Juego adivina mi número
import random

num=random.randint(1,20)
contador=0
while(True):
    if contador==5:
        print("No adivinaste, mi número era ",num)
        break
    numero=eval(input("ingresa un número: "))
    if numero==num:
        print("Adivinaste, mi número era ",num)
        break
    else:
        if numero<num:
            print("mi número es mayor")
        elif numero>num:
            print("mi número es menor")
        contador=contador+1