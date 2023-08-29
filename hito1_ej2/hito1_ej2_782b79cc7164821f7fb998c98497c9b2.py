telefono=input('Ingrese numero telefonico: ')
Hora=int(input('Ingrese hora de la llamada: '))

if Hora<=7 and Hora>=0:
  print('CONTESTAR')
  
if Hora>19:
  print('NO CONTESTAR')
  
if Hora==16 or Hora==15:
  print('NO CONTESTAR')

if Hora>7 and Hora<=13:
  if telefono[5:8]=='909':
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')

if Hora>=17 and Hora<19:
  if telefono[5:8]=='877':
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
  