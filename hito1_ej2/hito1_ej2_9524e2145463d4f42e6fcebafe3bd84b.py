llamada = (input('ingrese numero: '))
hora = int(input('ingrese hora: '))

if hora < 7:
  print('Resultado: CONTESTAR')

elif hora < 14 and llamada[5:8] == '909':
  print('Resultado: CONTESTAR')

elif hora < 14:
  print('Resultado: NO CONTESTAR')

elif 17 < hora < 19 and llamada[0:3] == '877':
  print('Resultado: NO CONTESTAR')

elif 17 < hora < 19:
  print('Resultado: CONTESTAR')

elif hora > 19:
   print('Resultado: NO CONTESTAR')
