#Aprobación de créditos
ingresos=int(input('Indique sus ingresos en pesos: '))
nacimiento=int(input('Ingrese su año de nacimiento: '))
hijos=int(input('Ingrese su numero de hijos: '))
banco=int(input('Ingrese sus años de pertenencia al banco: '))
C=1
S=2
R=1
U=2
estado=eval(input('Ingrese C si está casado y S si es soltero: '))
vivienda=eval(input('Ingrese R si vive en el campo y U si vive en ciudad: '))

edad = 2020-nacimiento

if 10 < banco and 2 <= hijos:
  print('APROBADO')
else:
  print('RECHAZADO')
  
if estado==C and 3 < hijos and 45 <= edad <= 55:
  print('APROBADO')
else:
  print('RECHAZADO')
  
if 2500000<ingresos and estado==S and vivienda==U:
  print('APROBADO')
else:
  print('RECHAZADO')
  
if 3500000<ingresos and 5<banco:
  print('APROBADO')
else:
  print('RECHAZADO')
  
if vivienda==R and estado==C and hijos<2:
  print('APROBADO')
else:
  print('RECHAZADO')
