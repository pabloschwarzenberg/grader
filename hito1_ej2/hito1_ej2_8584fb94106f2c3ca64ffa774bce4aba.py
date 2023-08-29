#Contestador de celular
c = True
while c: #restricción para que el numero sea de 8 digitos
    numero = int(input('Ingrese número telefónico: '))
    if len(str(numero)) == 8:
      c = False
    else:
      print ('Número telefónico ingresado debe contener exactamente 8 digitos')

c = True
while c: #restricción para que la hora sea entre 0 y 23
    hora = int(input('Ingrese hora de la llamada: '))
    if ((hora >= 0) and (hora <=23)):
      c = False
    else:
      print ('Hora de llamada debe ser entre 0 y 23')

if ((hora >= 0) and (hora <= 7)):
  print ('CONTESTAR')
elif ((hora > 7) and (hora < 14)):
  if ((str(numero)[5:8]) == '909'):
    print ('CONTESTAR')
  else:
    print ('NO CONTESTAR')
elif ((hora >= 17) and (hora <= 19)):
  if ((str(numero)[0:3]) == '877'):
    print ('NO CONTESTAR')
  else:
    print ('CONTESTAR')
else:
  print ('NO CONTESTAR')