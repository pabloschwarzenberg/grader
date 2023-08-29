#Juego adivina mi número

import random

i = 1
ran = random.randint(1,20)

while i :
  num = int(input("Ingrese numero: "))
  if num == ran:
     print("Adivinaste, mi número era ", num)
  else:
    i += 1
if( i == 7):
  print("No adivinaste, mi número era ", ran)


    