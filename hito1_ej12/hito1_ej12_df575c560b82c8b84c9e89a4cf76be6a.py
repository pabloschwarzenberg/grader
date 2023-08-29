#Juego adivina mi número
import random
a=random.randint(1,20)
i=0
for i in range(5):
    b=int(input("Posible número:"))
    if (a==b):
        print("Adivinaste")
        break
    elif (a>b):
        print("El número es mayor")
    elif (a<b):
        print("El número es menor")
    i=i+1
    print("Inténtalo de nuevo :)")
if (i==5):
    print("Mi número era:",a)

      