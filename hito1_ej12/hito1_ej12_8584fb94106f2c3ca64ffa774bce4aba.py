#Juego adivina mi número
import random #importar funcion random
numeroRandom = random.randint(1, 20) #randit -> retorna número entero aleatorio entre los números ingresados (1 y 20)
intentos = 0
c = True
while c:
  numero = int(input('[Intento '+str(intentos+1)+'/5] Ingrese número: '))
  intentos = intentos + 1
  if numero > numeroRandom:
    if intentos != 5:
     print('Mi número secreto es menor')
  elif numero < numeroRandom:
    if intentos != 5:
      print('Mi número secreto es mayor')
  else:
    print('Adivinaste, mi número era '+str(numeroRandom))
    c = False

  if (intentos == 5 and c == True):
    print('No adivinaste, mi número era '+str(numeroRandom))
    c = False   