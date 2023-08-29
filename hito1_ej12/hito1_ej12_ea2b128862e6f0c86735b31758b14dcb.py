#Juego adivina mi número
from random import *

numero_secreto=randint(0,21)

x=0

while(x<4):
    n1=int(input("Ingrese su primer intento: "))
    if(n1<numero_secreto):
        x+=1
        print("mi número es mayor")
    elif(n1==numero_secreto):
        print("Adivinaste, mi número era ",numero_secreto)
        break
    elif(n1>numero_secreto):
        x+=1
        print("mi número es menor")
    else:
        continue

    n2=int(input("Ingrese su segundo intento: "))
    if(n2<numero_secreto):
        x+=1
        print("mi número es mayor")
    elif(n2==numero_secreto):
        print("Adivinaste, mi número era ",numero_secreto)
        break
    elif(n2>numero_secreto):
        x+=1
        print("mi número es menor")
    else:
        continue
    
    n3=int(input("Ingrese su tercer intento: "))
    if(n3<numero_secreto):
         x+=1
         print("mi número es mayor")
    elif(n3==numero_secreto):
         print("Adivinaste, mi número era ",numero_secreto)
         break
    elif(n3>numero_secreto):
         x+=1
         print("mi número es menor")
    else:
        continue
         
    n4=int(input("Ingrese su cuarto intento: "))
    if(n4<numero_secreto):
        x+=1
        print("mi número es mayor")
    elif(n4==numero_secreto):
        print("Adivinaste, mi número era ",numero_secreto)
        break
    elif(n4>numero_secreto):
        x+=1
        print("mi número es menor") 
    else:
        continue
        
    n5=int(input("Ingrese su quinto intento: "))
    if(n5<numero_secreto):
        x+=1
        print("No adivinaste, mi número era ",numero_secreto)
    elif(n5==numero_secreto):
        print("Adivinaste, mi número era ",numero_secreto)
        break
    elif(n5>numero_secreto):
        x+=1 
        print("No adivinaste, mi número era ",numero_secreto)
    else:
        print("No adivinaste, mi número era ",numero_secreto)
