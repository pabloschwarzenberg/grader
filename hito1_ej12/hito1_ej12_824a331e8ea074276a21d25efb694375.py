#Juego adivina mi número
import random as rn

dig=rn.randint(1,20)
#dig=16
print(dig)
numero=int(input("ingrese numero :"))
contador=0
if numero==dig:
    print("Adivinaste, mi número era",dig)
    
else:
  while contador<=5:
    contador=contador+1  
    if numero>dig:
       print("mi número es mayor")
    if numero<dig:
        print("mi número es menor")
    if(numero==dig):
      print("Adivinaste, mi número era",dig) 
      break
       
    if contador==5:
        print("No adivinaste, mi número era ",dig)
        break
    numero=int(input("ingrese numero :"))
    