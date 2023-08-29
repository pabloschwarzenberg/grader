#Juego adivina mi número
import random 
a=random.randint(1,20)
print(a)
i=0

while i<5:
    b=int(input("ingrese un numero:"))
    if a==b:
        print("Adivinaste,mi número era:",a)
        break
    if a<b:
        print("mi número es menor")
        i+=1
    elif a>b:
        print("mi número es mayor")
        i+=1
else:
    print("No adivinaste, mi número era:",a)      