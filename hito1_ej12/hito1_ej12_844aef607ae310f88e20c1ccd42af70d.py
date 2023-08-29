#Juego adivina mi número
import random
secreto = random.randint(1,20)
n = 0
while n<5:
  numero = eval(input(''))
  if n == 4:
    print('No adivinaste, mi número era',secreto)
    break
  else:
    n +=1 
  if numero < secreto:
    print('mi numero es mayor')
  elif numero > secreto:
    print('mi numero es menor')
  elif numero == secreto:
    print('Adivinaste, mi numero era',secreto)
    break
