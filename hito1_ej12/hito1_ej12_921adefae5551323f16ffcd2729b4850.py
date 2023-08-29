#Juego adivina mi número
import random
z=0
x=(random.randrange(20))
while(z<5):
    
    print(x)
    turno=int(input(print("adivina mi numero")))
    if(turno==x):
        print("adivinasten mi numero era",x)
        break
    elif(turno<x):
        print("mi numero es mayor")
    elif(turno>x):
        print("mi numero es menor")
    z=z+1
if(z==5):
    print("No adivinaste, mi numero era",x)      