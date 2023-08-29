#Juego adivina mi número
import random

intentos = 0
numero = random.randint(1,20)
print('estoy pensando en un numero entre 1 y 20')

while intentos<5:
  print ('Intenta adivinar')
  estimacion = input()
  estimacion = int(estimacion)

  
  if estimacion<numero:
   print ('el numero es menor')
   intentos = intentos +1
   
  if estimacion>numero:
   print ('el numero es mayor')
   intentos = intentos +1
   
  if estimacion==numero:
    break

if estimacion==numero:
  intentos = str(intentos)
  numero = str(numero)
  print('Adivinaste, mi número era'+' '+numero+' '+'Haz adivinado numero en'+' '+intentos+' '+'intentos')


if estimacion !=numero:
  numero = str(numero)
  print('No adivinaste, mi número era'+' '+numero)
  
