#Juego adivina mi número
import random
a = random.randrange(21)
b = int(input("Ingrese numero b:"))
count = 0
while count < 5 and a!=b :
        if a < b :
            b=int(input())
        elif a > b :
            b=int(input())
        count = count + 1
if a==b :
    print("Adivinaste, mi número era" , a)
else :
    print("No adivinaste, mi número era" , a)


