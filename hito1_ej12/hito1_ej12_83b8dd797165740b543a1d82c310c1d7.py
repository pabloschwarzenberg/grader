import random
numero = random.randint(1,20)
intentos = 5

while intentos > 0:
      respuesta = int(input('Ingrese un numero: '))
      if respuesta < numero:
        print('mi número es mayor')
        intentos -= 1
      elif respuesta > numero:
        print('mi número es menor')
        intentos -= 1
      else:
        print('Adivinaste, mi número era',numero)
       

if intentos == 0:
    print('No adivinaste, mi número era',numero)
    
    