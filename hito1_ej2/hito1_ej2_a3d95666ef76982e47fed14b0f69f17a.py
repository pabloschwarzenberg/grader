D=range(20,23)
R=range(17,19)
T=range(8,14)
U=range(15,16)
emergencia= range(8)

#numero
numero=int(input('ingrese numero: '))
while numero<10000000 or numero>100000000:
  numero=int(input('ingrese numero nuevamente:'))

#hora
hora=int(input('ingrese hora de llamada: '))
while hora>23 or hora<0:
  hora=int(input('ingrese hora de llamada nuevamente: '))

if hora in emergencia:
  print('>contestar por emergencia<')

if hora in T:
  if str(numero)[-3:]=='909':
     print('>contestar, es una emergencia<')
  else:
     print('>no conestar<')

if hora in R:
  if not str(numero)[:3]=='877':
    print('>contestar<')
  else:
    print('NO CONTESTAR')

if hora in D:
  print('NO CONTESTAR')

if hora in U:
  print('>estamos en colacion<')