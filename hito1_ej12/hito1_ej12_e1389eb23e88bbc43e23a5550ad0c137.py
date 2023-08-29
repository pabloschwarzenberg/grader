#Juego adivina mi número
import random
a=random.randint (1,20)
i=0
while i<5:
  print("adivina un numero entre 1 y 20")
  n=int(input("numero="))
  if n==a:
    print("Advinaste, mi numero era", a)
  elif n<a:
    i=i+1
    print("No adivinaste, el numero es mayor que",n)
  elif n>a:
    i=i+1
    print("No adivinaste, el numero es menor que",n)
if i==5:
  print("No adivinaste, mi numero era", a)