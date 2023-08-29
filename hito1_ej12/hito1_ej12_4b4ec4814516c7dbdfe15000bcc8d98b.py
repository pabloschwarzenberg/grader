import random
import sys
numero=random.randint(1,20)

contador=1
while contador<=5:
    x=int(input("Ingrese un numero del 1 al 20:"))
    
    if numero==x:
       print("Adivinaste, mi numero era",numero)
       break 
    elif numero>x:
       print("El numero que tienes que adivinar es mayor")
    elif numero<x:
       print("El numero que tienes que adivinar es menor")
    contador+=1
    
if contador>5:
    print("No adivinaste, mi numero era",numero)    
