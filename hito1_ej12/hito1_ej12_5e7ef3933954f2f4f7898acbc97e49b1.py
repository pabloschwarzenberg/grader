import random

numero = random.randint(1, 20)
intentosRealizados = 0
numero = 7
while intentosRealizados < 5:
    estimacion = input("ingresa numero :")
    estimacion = int(estimacion)
    intentosRealizados = intentosRealizados + 1
    if estimacion < numero:
       print('mayor')
    if estimacion > numero:
        print('menor')
    if estimacion == numero:
        break
if estimacion == numero:
   intentosRealizados = str(intentosRealizados)
   print('Adivinaste, mi número era',numero)
if estimacion != numero:
  numero = str(numero)
  print('No adivinaste, mi número era',  numero)

