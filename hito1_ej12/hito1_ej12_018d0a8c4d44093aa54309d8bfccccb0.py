#Juego adivina mi número
import random
r= random.randint(1,20)
intentos=1
while intentos<=5:
    a= int(input())
    if a<r:
        print("mayor")
    elif a>r:
        print("menor")
    elif a==r:
        print("Adivinaste, mi numero era ",r)
        break
    intentos+=1
    if intentos==0:
        print("No adivinaste, mi numero era "+str(r)+"")