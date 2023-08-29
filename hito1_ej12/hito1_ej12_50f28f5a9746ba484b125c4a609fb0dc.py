from os import system
import random
system("cls")

ver=0
ran=random.randint(1, 20)

for i in range(5):
    while True:
        num=int(input("Adivina mi numero: "))
        if num==ran:
            ver=1
            break
        elif num>ran:
            print("mi numero es menor")
            break
        else:
            print("mi numero es mayor")
            break
if ver==1:
    print("Adivinaste, mi numero era:" ,ran)
else:
    print("No adivinaste, mi número era:",ran )