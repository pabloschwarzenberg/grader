#Juego adivina mi número
import random
intentosRealizados = 5
numero = random.randint(1, 20)
print('estoy pensando en un número entre 1 y 20.')
  while intentosRealizados < 6:
    print('Intenta adivinar.')
    estimacion = input()
    estimacion = int(estimacion)
    intentosRealizados = intentosRealizados + 1
    if estimacion < numero:
      print('mi numero es menor.')
    if estimacion > numero:
      print('mi número es mayor')
    if estimacion == numero:
      break
if estimacion == numero:
  intentosRealizados = str(intentosRealizados)
  print('¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')
if estimacion != numero:
  numero = str(numero)
  print('Mi numero era:' + numero)