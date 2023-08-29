#Juego adivina mi número
import random
a=int(input())
b=random.randint(1,20)
for i in range(5):
  if a<b:
    print("mi número es mayor")
  elif a>b:
    print("mi número es menor")
  else:
    print("Adivinaste, mi número era",b)
    break
print("No adivinaste, mi número era",b)