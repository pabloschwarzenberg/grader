#Aprobación de créditos
ingreso=eval(input('ingreso:'))
nacimiento=int(input('año de nacimiento:'))
hijos=int(input('numero de hijos:'))
pertenencia=int(input('años de pertenencia en el banco:'))
estado=input('estado civil ("S": soltero, "C", casado):')
lugar=input('usted vive en campo o cuidad ("U": urbano, "R": rural):')

print('\n')

if (pertenencia>=10 and hijos>=2) or (estado=='C' and hijos>=3 and 1965<=nacimineto<=1975)\
 or (ingreso>=2500000 and estado=='S' and lugar=='U') or (ingreso>=3500000 and pertenencia>=5)or (estado=='C' and lugar=='R' and hijos<2)  :
  print('APROBADO')
else:
  print('RECHAZADO')
  