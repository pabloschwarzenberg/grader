#Contestador de celular
a=input('Ingrese numero de telefono: ')
b=int(input('Ingrese hora de llamada: '))
e0=a[0]
e1=a[1]
e2=a[2]
e5=a[5]
e6=a[6]
e7=a[7]
if b>=0 and b<=7:
  print('CONTESTAR')
elif (b>=8 and b<=14):
  if e5=='9' and e6=='0' and e7=='9':
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
elif b==17 or b==18 or b==19:
  if e0=='8' and e1=='7' and e2=='7':
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
else:
  print('NO CONTESTAR')      