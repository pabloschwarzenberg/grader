#Juego adivina mi número
import random
secreto=random.randint(1,20)
i=0
while i<5:
    num=int(input("Ingrese numero:"))
    if num==secreto:
        print("Adivinaste, mi numero era",secreto)
        break
    elif num>secreto:
        print("mi número es menor")
    elif num<secreto:
        print("mi número es mayor")
    i=i+1
if i==5:
    print("No adivinaste, mi número era",secreto)