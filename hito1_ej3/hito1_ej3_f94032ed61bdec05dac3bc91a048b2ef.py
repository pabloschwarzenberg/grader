print('Ingrese sus datos: ')

ingreso = int(input('Ingresos: '))
ano = 2022 - int(input('Cuantos años tiene: '))
hijos = int(input('Cuantos hijos tiene: '))
anoB = int(input('Años en el banco: '))
estado_civil = input('Estado civil S: soltero C:"Casado: ')
vive = input('Vive en zona rural(R) o en zona urbana(U): ')


min = 2500000
max = 3500000

if anoB > 10 and hijos >= 2:
  print('APROBADO')
if estado_civil == "C" or estado_civil == "c" and hijos > 3 and ano > 45 and ano < 55:
  print('APROBADO')
if ingreso > min and estado_civil == "s" or estado_civil == "S" and vive == "u" or vive == "U":
  print('APROBADO')
if ingreso > max and anoB > 5:
  print('APROBADO')
if vive == "R" or vive == "r" and hijos < 2:
  print('APROBADO')
print('DENEGADO')