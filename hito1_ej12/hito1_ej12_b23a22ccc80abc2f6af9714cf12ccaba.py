#Juego adivina mi número
import random
y=random.randint(1,20)
for x in range(5):
  x=int(input("ingrese un numero entre 1 y 20:"))
  if(x>y):
    print("mi número es menor")

  if(x<y):
    print("mi número es mayor")
 
  if(x==y):
    print ("Adivinaste, mi número era", y)
      
if(x!=y):
  print("No adivinaste, mi número era", y)