#Juego adivina mi número
import random
a=(random.randrange(20)) 
for i in range(0,5):
  num=int(input("ingrese el numero que cree que es(del 1 al 20): "))
  if a==num:
    print("Adivinaste, mi número era ",num)
    break
  elif a<num:
    print("No adivinaste, mi número es menor")
  elif a>num:
    print("No adivinaste, mi número es mayor")
print("No adivinaste, mi número era: ",a)