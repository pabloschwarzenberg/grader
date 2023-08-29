#Juego adivina mi número
import random
i=random.randint(1,20)
c=0
while(c<5):
      n=int(input("Ingrese un número:"))
      if(n<i): 
        print("Su número es menor al secreto:")
        c=c+1
      elif(n>i): 
        print("Su número es mayor al secreto:")
        c=c+1
      else: 
        print("Adivinaste, mi número era",n)
        break
if(c==5): 
  print("No adivinaste, mi número era",n)