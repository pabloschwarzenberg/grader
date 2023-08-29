#Juego adivina mi número
import random 
a=random.randint(1,21)
j=0 
while j<5:
    n=int(input("ingresa tu numero:"))
    if (n<a):
       print ("Tu numero es menor")
       j=j+1
    elif (n>a):
       print("Tu numero es mayor")
       j=j+1
    elif (n==a):
       print("Adivinaste, mi número era:",a) 
       break
if j==5: 
     print("No adivinaste, mi número era",a) 