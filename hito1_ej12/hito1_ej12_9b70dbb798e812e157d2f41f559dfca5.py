#Juego adivina mi número
import random
a=random.randint(1, 20)
i=0
while i<5:
  b=int(input("adivine el numero que esta entre 1 y 20: "))
  if b<a:
    print("el numero es mayor")
  if b>a:
    print("el numero es menor")
  if b==a:
    print("Adivinaste, mi numero era", a)
    break
  i=i+1
else:
  print("No adivinaste, mi numero era", a)      