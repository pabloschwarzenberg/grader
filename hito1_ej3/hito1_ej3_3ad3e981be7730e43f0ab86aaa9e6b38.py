ingresos = int(input("indique sus ingresos en pesos: "))
nacimiento = int(input("ingrese su fecha de nacimiento: "))
num_hijos = int(input("ingrese el numero de hijos que posee: "))
time_banco = int(input("cuanto tiempo ha pertenecido al banco: "))
estado_civil = input('soltero "S" o cadaso "C": ')
vivienda = input('vive en zona urbana "U" o en zona rural "R": ')
edad = 2023-nacimiento

if time_banco>10:
  print('APROBADO')
else:
    print('RECHAZADO')
if (estado_civil=='C') and (num_hijos>3) and (edad>=45 and edad<=55):
  print('APROBADO')
else:
    print('RECHAZADO')
if ingresos>2500000 and estado_civil=='S' and vivienda=='U':
  print('APROBADO')
else:
    print('RECHAZADO')
if ingresos>3500000 and time_banco>5:
  print('APROBADO')
else:
    print('RECHAZADO')
if vivienda=='R' and estado_civil=='C' and num_hijos<2:
  print('APROBADO')
else:
    print('RECHAZADO')