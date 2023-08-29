numero = int(input('ingrese numero telefonico: '))
hora = int(input('ingrese hora de la llamada: '))

if hora >= 0 and hora <= 7:
  print('resultado:CONTESTAR')
elif hora <= 14:
  digito = numero % 1000
  if digito == 909:
    print('resultado:CONTESTAR')
  else:
    print('resultado:NO CONTESTAR')
elif hora >= 17 and hora <= 19:
  digito = numero // 100000
  if digito == 877:
    print('resultado:NO CONTESTAR')
  else:
    print('resultado: CONTESTAR')
elif hora > 19:
  print('resultado: NO CONTESTAR')
  