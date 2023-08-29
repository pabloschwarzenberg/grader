#Juego adivina mi número
import random
intentosRealizados = 0
número = random.randint(1, 20)
while intentosRealizados < 5:
  print('Intenta adivinar.')
  estimación = input()
  estimación = int(estimación)
  intentosRealizados = intentosRealizados + 1
  if estimación < número:
    print('mi numero es mayor.')
  if estimación > número:
    print('mi número es menor.')
  if estimación == número:
    break
if estimación == número:
  intentosRealizados = str(intentosRealizados)
  print("Adivinaste, mi número era " + str(número))
if estimación != número:
  número = str(número)
  print('No adivinaste. mi número era ' + número)