ingreso = int(input('Ingrese sus ingresos en pesos: '))
nacimiento = int(input('Ingrese su año de nacimiento: '))
hijos = int(input('Ingrese la cantidad de hijos que tiene: '))
pertenencia = int(input('Ingrese los años de pertenencia al banco: '))
estadocivil = input('Ingrese su estado civil, con una S si está soltero, o una C si está casado: ')
vive = input('Ingrese una U si vive en la ciudad, o una R si vive en el campo: ')

if pertenencia > 10 and hijos >= 2:
  print('APROBADO')
elif estadocivil == 'c' and hijos > 3 and nacimiento > 1967 and nacimiento < 1977:
  print('APROBADO')
elif ingreso > 2500000 and estadocivil == 'S' and vive == 'U':
  print('APROBADO')
elif ingreso > 3500000 and pertenencia > 5:
  print('APROBADO')
elif vive == 'R' and estadocivil == 'C' and hijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')