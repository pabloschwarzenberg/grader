#Contestador de celular
z=input('ingrese el numero de telefono: ')
c=int(input('ingrese la hora de la llamda: '))
j=z[0]+z[1]+z[2]
y=z[5]+z[6]+z[7]
if(c<=7):
 print('CONTESTAR')
if(7<c<14 and y=='909'):
 print('CONTESTAR')
elif(7<c<14):
  print('NO CONTESTAR')
if(17<c<19 and j=='877'):
  print('NO CONTESTAR')
elif(14<c<17):
  print('NO CONTESTAR')
elif(17<c<19):
  print('CONTESTAR')
if(c>19):
  print('NO CONTESTAR')