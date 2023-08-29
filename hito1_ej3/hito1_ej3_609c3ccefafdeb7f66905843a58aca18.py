#
ingreso=int(input('ingreso en peso: '))
annos=int(input('ingrese su año de nacimiento: '))
hijos=int(input('numero de hijos :'))
anosbanco=int(input('ingrese años de banco: '))
estado=input('ingrese su estado civil (s: soltero, c: casado): ')
vivir=input('ingrese si vive en el campo o ciudad: (u\r)')
if anosbanco>=10 and hijos>=2:
  print('APROBADO')
elif estado=='C' and hijos>=3 and annos<=55 and 45<=annos:
  print('APROBADO')
elif ingreso>=2500000 and EC=='S' and vivir=='U':
  print('APROBADO')
elif ingreso>=3500000 and anosbanco>=5:
  print('APROBADO')
elif vivir=='R' and estado=='C' and hijos<=2:
  print('APROBADO')
else:
  print('RECHAZADO')