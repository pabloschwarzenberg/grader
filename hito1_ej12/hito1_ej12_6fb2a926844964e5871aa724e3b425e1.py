#Juego adivina mi número
intentos=5
import random
N=random.randint(1,20)
print("tienes cinco intentos para adivinar el numero")


while (intentos > 0):
     V=int(input("ingrese numero:"))
    
     if (N==V): 
       print("usted acerto el numero")
       break
           
     else:
         if(N > V):
           print("el numero secreto es mayor que su numero")
         if(N < V):
           print("su numero es mayor que el numero secreto")
         intentos=intentos-1

if(intentos==0):
  print("no adivinaste, el numero era",N)              
