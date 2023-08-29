#Contestador de celular
tel = int(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))

respuesta = ' '
if hora >= 0 and hora <= 7:
  respuesta = 'CONTESTAR'
  
elif hora >= 8 and hora <= 14:
  if str(tel)[5:] == '909':
    respuesta = 'CONTESTAR'
  else:
    respuesta = 'NO CONTESTAR'
    
elif hora >= 15 and hora <= 19:
    if str(tel)[:3] == '877':
        respuesta = 'NO CONTESTAR'
    else:
        respuesta = 'CONTESTAR'
    
else:
    respuesta = 'NO CONTESTAR'

print('Respuesta: {0}'.format(respuesta))