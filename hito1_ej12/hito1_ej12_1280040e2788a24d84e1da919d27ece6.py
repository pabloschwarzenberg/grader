#Juego adivina mi número
import random
x=random.randint(1,20)
contador=0
while contador<5:
 numero=int(input("adivina mi numero entre 1 al 20 : "))
 if(numero<x):
  print("mi numero es mayor")
  contador+=1
 elif(numero>x):
  print("mi numero es menor")
  contador+=1
 elif(numero==x):
  print("Adivinaste, mi numero era ",x)
  break
if(contador==5):
 print("No adivinaste, mi numero era ",x)