#Aprobación de créditos
 
sueldo=int(input('Ingrese su sueldo en pesos: '))
nacimiento=int(input('Año de nacimiento: '))
hijos=int(input('Numero de hijos: '))
pertenencia=int(input('Años de pertenencia al banco: '))
estado=str(input('Estado civil ("S":soltero o "C":casado): '))
zona=str(input('Zona donde vive("U":urbano o "R":rural): '))

edad= 2020-nacimiento

print('\n')

if pertenencia>10 and hijos>=2:
  print('APROBADO')
elif estado=='C' and hijos>3 and 45<edad<55:
  print('APROBADO')
elif sueldo>2500000 and estado=='S' and zona=='U':
  print('APROBADO')
elif sueldo>3500000 and pertenencia>5:
  print('APROBADO')
elif zona=='R' and estado=='C' and hijos<2:
  print('APROBADO')
else:
  print('RECHAZADO')