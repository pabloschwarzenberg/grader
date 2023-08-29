n=input('numero de telefono de 8 cifras: ')
h=int(input('hora de llamada: '))
exc0=n[0]
exc1=n[1]
exc2=n[2]
exc5=n[5]
exc6=n[6]
exc7=n[7]
if h>=0 and h<=7:
  print('CONTESTAR')
elif (h>=8 and h<=14):
  if exc5=='9' and exc6=='0' and exc7=='9':
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
elif h==17 or h==18 or h==19:
  if exc0=='8' and exc1=='7' and exc2=='7':
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
else:
  print('NO CONTESTAR')