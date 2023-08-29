#Contestador de celular
n = int(input('Ingrese el número telefónico'))
h = int(input('Ingrese hora de la llamada'))
if h == 0 or h == 1 or h == 2 or h == 3 or h == 4 or h == 5 or h == 6 or h == 7:
  print('CONTESTAR')
if h == 8 or h == 9 or h == 10 or h == 11 or h == 12 or h == 13:
  if n % 1000 == 909:
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
if h == 17 or h == 18 or h == 19:
  if n // 100000 == 877:
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
if h == 20 or h== 21 or h == 22 or h == 23:
  print('NO CONTESTAR')


