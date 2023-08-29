#Contestador de celular
numero_telefonico = int(input('ingrese el numero telefonico de (8 cifras): '))
hora = int(input('ingrese la hora de la llamada(0-23): '))

if 0 <= hora <= 7:
  print('CONTESTAR')

elif 7 <= hora < 14:
  if numero_telefonico % 1000 == 909:
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
    
elif 15 <= hora < 19:
  if numero_telefonico // 100000 == 877:
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
  
if 19 <= hora:
  print('NO CONTESTAR')