#Juego adivina mi número
import random

n_secreto = random.randint(1,20)
intentos = 5
vidas = intentos
while vidas >= 0:
    intento = int(input('Ingrese su intento {}: '.format(vidas)))
    if vidas == 1:
      print('No adivinaste, mi número era {}'.format(n_secreto))
      break
    if intento == n_secreto:
      print('Adivinaste, mi número era {}'.format(n_secreto))
      break
    elif intento < n_secreto and vidas > 0:
      vidas = vidas - 1
      print('mi número es mayor')
      continue
    elif intento > n_secreto and vidas > 0:
      vidas = vidas - 1
      print('mi número es menor')
      continue