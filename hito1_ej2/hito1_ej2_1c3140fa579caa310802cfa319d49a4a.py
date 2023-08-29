#Contestador de celular

while(1):
  celu=int(input('Ingrese numero telefonico de 8 digitos:'))
  hora=int(input('Ingrese hora de la llamada (responda entre 0 y 23):'))

  if(hora>=0 and hora<=7):
    print('CONTESTAR')

  if(hora>=8 and hora<=14 and str(celu)[5:8] !='909'):
    print('NO CONTESTAR')

  if(hora>=8 and hora<=14 and str(celu)[5:8] =='909'):
    print('CONTESTAR')

  if(hora>=17 and hora<=19 and str(celu)[0:3]!='877' ):
    print('CONTESTAR')

  if(hora>=17 and hora<=19 and str(celu)[0:3]=='877' ):
    print('NO CONTESTAR')

  if(hora>=20 and hora<=23):
    print('NO CONTESTAR')