#Juego adivina mi número
import random
M=random.randrange(1,20)
i=1
while(i<=5):
  n=int(input())
  if (n<M):
    print("El numero es menor que el numero secreto")
  elif (n>M):
    print("El numero es mayor que el numero secreto")
  elif (n==M):
    print("Adivinaste, mi número era", M)
    break
  i=i+1
print("No adivinaste, mi número era", M)