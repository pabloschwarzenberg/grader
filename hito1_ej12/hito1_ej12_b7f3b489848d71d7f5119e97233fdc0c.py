import random

intentosRealizadosss = 0
numero = random.randint(1, 20)

print('Bueno, estoy pensando en un número entre 1 y 20.')

while intentosRealizadosss < 5:
  print('Intenta adivinar.') 
  estimacion = input ("Diga numero")
  estimacion = int (estimacion)

  intentosRealizadosss = intentosRealizadosss + 1
  if estimacion == 11:
    print("Entonces")

  if estimacion < numero:
    print('mi número es menor.') 
  if estimacion > numero:
    print('mi número es mayor.')  
  if estimacion == numero:
    print('¡Adivinaste, mi número era',estimacion)
    break
if estimacion != numero:
  numero = str(numero)
  print('No adivinaste , mi número era ' + numero)