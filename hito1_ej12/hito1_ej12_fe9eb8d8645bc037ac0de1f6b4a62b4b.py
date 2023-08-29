#Juego adivina mi número
import random
while True:
  n=random.randint(1,20)
  a=int(input("Adivina el numero del 1 al 20, primer intento"))
  if a==n:
    break
  elif a>n:
    print("Mayor")
  else:
    print("Menor")
  b=int(input("Adivina el numero del 1 al 20, segundo intento"))
  if b==n:
    break
  elif b>n:
    print("Mayor")
  else:
    print("Menor")
  c=int(input("Adivina el numero del 1 al 20, tercer intento"))
  if c==n:
    break
  elif c>n:
    print("Mayor")
  else:
    print("Menor")
  d=int(input("Adivina el numero del 1 al 20, cuarto intento"))
  if d==n:
    break
  elif d>n:
    print("Mayor")
  else:
    print("Menor")
  e=int(input("Adivina el numero del 1 al 20, quinto intento"))
  if e==n:
    print("Adivinaste, mi numero era",n)
    break
  else:
    print("No adivinaste, el numero era ",n)
    break