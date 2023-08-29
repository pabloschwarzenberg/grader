#Juego adivina mi número
import random
sec = random.randint(1,20)
b = 0
i = 0
while i <= 5:
  b = input()
  b = int(b)
  if sec == b:
    print("Adivinaste, mi número era", sec)
    break
  else:
    if b > sec:
      print("Mi número es menor") 
    elif b < sec:
      print("Mi número es mayor")
  i += 1
  if i == 5:
    print("No adivinaste, mi número era", sec)