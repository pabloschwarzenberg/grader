#Juego adivina mi número
intentos=5
N=5
import random 
N=random.randint(1,20)
print("tienes 5 intentos para adivinar el numero secreto:")
while(intentos > 0):
  M=int(input("ingresa el numero que usted piensa que es:"))
  if (M==N):
    print("adivinaste, el numero era", N)
    break
  else:
    if(M < N):
      print("tu nomero es menor a mi numero secreto")
    if(M > N):
      print("tu numero es mayor a mi numero secreto")
    intentos=intentos-1    
    
if (intentos==0):
    print("no adivinaste, mi numero era ",N)