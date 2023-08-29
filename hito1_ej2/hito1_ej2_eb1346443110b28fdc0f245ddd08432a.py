#Contestador de celular
t = int(input('Introduce telefono: '))

h = int(input('Introduce hora de llamada: '))


ni = t // 1000
ni2 = ni * 1000
nf = t - ni2
t2 = t // 100000

if  7 >= h >= 0 :
  print('CONTESTAR')

if 14 > h > 7 :
  if nf == 909:
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')


if 19 >= h >= 17:
  if t2 == 877:
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
    
if 23 >= h > 19:
  print('NO CONTESTAR')