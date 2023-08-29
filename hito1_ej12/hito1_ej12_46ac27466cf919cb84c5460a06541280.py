#Juego adivina mi número
import random
numero_adivinar = random.randint(1,20)
intentos = 0 
while intentos < 5:
  numero = int(input('Ingrese numero: '))
  if numero < numero_adivinar:
    print('mi numero es mayor')
  elif numero > numero_adivinar:
    print('mi numero es menor')
  else:
    print('Adivinaste, mi número era ', numero_adivinar)
    break
  intentos += 1
if intentos == 5:
  print('No adivinaste, mi número era ', numero_adivinar)