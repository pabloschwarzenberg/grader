import random

numero= random.randint(1,20)

i=0
while i<5:
  adivinar=int(input('Adivina el numero:'))
  if adivinar==numero:
    print("Adivinaste, mi número era ",numero)
    break
  else:
    if adivinar>numero:
      print('mi número es menor')
    elif adivinar<numero:
      print('mi número es mayor')
  i=i+1
  if i == 5:
    print("No adivinaste, mi número era ",numero)