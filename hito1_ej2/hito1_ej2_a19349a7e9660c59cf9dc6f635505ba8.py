#Contestador de celular
numero= (input('Ingrese el numero telefonico '))
hora= int(input('Ingrese la hora de la llamada '))

if hora>=0 and hora<=7:
  print('\n','CONTESTAR')
elif hora<14:
  if numero.endswith('909'):
    print('\n','CONTESTAR')
  else:
    print('\n','NO CONTESTAR')
elif hora >= 17 and hora <= 19:
  if numero.startswith('877'):
    print('\n','NO CONTESTAR')
  else:
    print('\n','CONTESTAR')
else:
  print('NO CONTESTAR')  