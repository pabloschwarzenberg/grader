#Contestador de celular
telefono=int(input('dame el numero'))
hora=int(input('dame la hora'))
telefono=str(telefono)
if 0<hora<0.7:
  print('Resultado:CONTESTAR')
if hora<14:
  telefono=str(telefono)
  if telefono[5]+telefono[6]+telefono[7]=='909' :
    print('Resultado:CONTESTAR')
  else:
    print('Resultado: NO CONTESTAR')
if 17<hora<19:
  telefono=str(telefono)
  if telefono[0]+telefono[1]+telefono[2]=='877':
    print('Resultado: NO CONTESTAR')
  else:
    print('Resultado: CONTESTAR')
if hora>19:
  print('Resultado: NO CONTESTAR')