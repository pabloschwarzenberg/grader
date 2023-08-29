#Contestador de celular
T=input('numero de telefono de 8 cifras: ')
H=int(input('hora de llamada: '))
exc0=T[0]
exc1=T[1]
exc2=T[2]
exc5=T[5]
exc6=T[6]
exc7=T[7]
if H>=0 and H<=7:
  print('CONTESTAR')
elif (H>=8 and H<=14):
  if exc5=='9' and exc6=='0' and exc7=='9':
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
elif H<=17 and H>=19:
  if exc0=='8' and exc1=='7' and exc2=='7':
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
else:
  print('NO CONTESTAR')