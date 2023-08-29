#Juego adivina mi número
import random
numero=int(input())
l=random.randint(1,20)
c=0
if numero==l:
  print ("adivinaste, mi número era ",l)
while c<5:
  if numero<l:
     print("mi número es mayor")
     c+=1
  if numero>l:
     print("mi número es menor")
     c+=1
     
print("No adivinaste, mi número era ",l)
 
