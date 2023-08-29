#Contestador de celular
n = input('Ingrese número telefonico:')
h = int(input('Ingrese hora de la llamada:'))
if h >= 0 and h <= 7:
   print('CONTESTAR')
if h > 7 and h <= 14:
  if n[5:] == '909':
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
if h >= 17 and h <= 19:
  if n[0:3] == '807':
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
if h > 19:
  print('NO CONTESTAR')
   