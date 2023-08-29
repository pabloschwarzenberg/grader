#Aprobación de créditos
ingreso=int(input('Ingreso (en pesos): '))
ano=int(input('Año de nacimiento: '))
hijos=int(input('Número de hijos: '))
apb=int(input('Años de pertenencia al banco'))
estado=input('Estado civil ("S": soltero, "C": casado: ')
localidad=input('Vive en campo o cuidad ("U": urbano, "R": rural: )')
edad=2023-ano

if apb>10 and hijos>=2:
  r='APROBADO'
elif estado=='C' and hijos>3 and 45<edad<55:
  r='APROBADO'
elif ingreso>2500000 and estado=='S' and localidad=='U':
  r='APROBADO'
elif ingreso>3500000 and apb>5:
  r='APROBADO'
elif localidad=='R' and estado=='C' and hijos<2:
  r='APROBADO'
else:
  r='RECHAZADO'

print(r)      