#Aprobación de créditos
ingreso=int(input('Ingreso: '))
adn=int(input('Año de nacimiento: '))
adn=2021-adn
nh=int(input('Número de hijos: '))
apb=int(input('Años de pertenencia al banco: '))
ec=input('Estado civil "S": soltero, "C", casado): ')
if ec=="S":
  ec=1
else:
  ec=0
coc=input('Si vive en campo o cuidad "U": urbano, "R": rural: ')
if coc=="U":
  coc=1
else:
  coc=0


if apb > 10 : 
  if nh >= 2:
    print('APROBADO')
if ec == 0:
  if nh>3:
     if 45>adn>55:
      print('APROBADO')
if ingreso>2500000: 
  if ec==1: 
    if coc==1:
      print('APROBADO')
if ingreso>3500000: 
  if apb>5 :
    print('APROBADO')
if coc==0 :
  if ec==0: 
    if nh<2 :
      print('APROBADO')
else:
  print('RECHAZADO')