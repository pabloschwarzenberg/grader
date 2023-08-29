#Juego adivina mi número
import random
xxx=(random.randrange(20))
for x in range(0,5):
   numero=int(input('adivine el numero (del 1 al 20): '))
   if xxx==numero:
     print('adivinaste, el numero era:',numero)
     break
   elif xxx>numero:
     print('el numero es mayor,')
   elif xxx<numero:
     print('el numero es menor,')

print('no adivinaste el numero era: ',xxx)