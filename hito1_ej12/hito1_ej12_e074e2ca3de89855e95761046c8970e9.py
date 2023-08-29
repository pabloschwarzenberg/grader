from random import *
num = randint(1,21)

print('El número oculto es: ', num)

for intento in range(1,6):
  print('Intento número: ',intento)
  num_ingresado = int(input('Ingrese un número: '))
 
  if num > num_ingresado:
    print('El número oculto es mayor a su número ingresado')
  elif num < num_ingresado:
    print('El número oculto es menor a su número ingresado')
  elif num == num_ingresado:
    print('Haz acertado al número oculto')
    break

if intento ==5:
  print('Haz agotado tus intentos')