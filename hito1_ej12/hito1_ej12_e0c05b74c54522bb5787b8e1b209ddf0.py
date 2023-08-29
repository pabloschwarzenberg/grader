#Juego adivina mi número
import random
a=random.randint(1,21)
b=5
while b>0:
  c=int(input())
  if c>a:
    print("mi número es mayor")
    b=b-1
  elif c<a:
    print("mi número es menor")
    b=b-1
  else:
    print("Advinaste, mi numero era",a)
    break
if b==0:
  print("No adivinaste, mi número era",a)
    