#Juego adivina mi número
import random
intentosRealizados = 0
numero = random.randint(1, 20)
while intentosRealizados < 5:
  print('Intenta adivinar.') # Hay cuatro espacios delante de print.
  estimacion = input()
  estimacion = int(estimacion)
  if estimacion < numero:
    print('Mi numero es mayor') 
  if estimacion > numero:
    print('Mi numero es menor')
  if estimacion == numero:
    break
  if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')
  if estimacion != numero:
    numero = str(numero)
    print('Pues no. El número que estaba pensando era ' + numero)