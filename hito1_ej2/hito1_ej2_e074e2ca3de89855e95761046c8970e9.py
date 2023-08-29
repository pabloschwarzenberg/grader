celular = str(input('Ingrese el número de celular, de 8 cifras, del cual llama: '))
hora = int(input('Ingrese la hora del día, representada por un entero, en la que llama: '))


if hora >= 0 and hora <= 7:
  print('CONTESTAR')

elif hora < 14 and celular[-3:] == '909':
  print('CONTESTAR')

elif hora < 14:
  print('NO CONTESTAR')

elif hora >= 17 and hora <= 19 and not celular[0:3] == '877':
  print('CONTESTAR')

elif hora >= 17 and hora <= 19:
  print('NO CONTESTAR')

elif hora >= 19:
  print('NO CONTESTAR')