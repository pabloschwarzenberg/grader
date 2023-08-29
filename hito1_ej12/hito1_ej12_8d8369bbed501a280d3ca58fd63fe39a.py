#Juego adivina mi número
import random
x=(random.randrange(0,21))
a=0
while a<5:
  f=int(input("Adivina mi número ---> "))
  
  if f==x:
    print("Adivinaste, mi número era ",x)
    a=a+10
  elif x<f:
   print("mi número es menor")
   a=a+1
  elif x>f:
    print("mi número es mayor")
    a=a+1
if a==5:
  print("No adivinaste, mi número era ",x) 