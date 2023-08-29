#Juego adivina mi número
import random
b=random.randint(1,20)
contador=0
while contador<=4:
    a=int(input("elige un numero"))
    if a>b:
        print("menor")
        contador+=1
    elif a<b:
        print("mayor")
        contador+=1
    elif a==b:
        print("correcto")