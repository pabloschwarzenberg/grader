#Aprobación de créditos
ingreso = float(input('Monto de sus ingresos: '))
nacimiento = float(input('Fecha de nacimiento: '))
hijos = float(input('Cantidad de hijos: '))
anos_banco = float(input('Años que ha pertenecido al banco: '))
estado_civil = input('Estado civil ("S": soltero, "C", casado): ')
vivienda = input('Vive en "U": urbano, "R": rural: ')

edad = 2020 - nacimiento
c = 2
C = 2
s = 1
S = 1
U = 1
u = 1
R = 2
r =2

if anos_banco >= 10 and hijos >= 2:
  print('APROBADO')
else:
  pass
  if estado_civil == 1 and hijos >= 3 and 45 <= edad <= 55:
    print('APROBADO')
  else:
    pass
    if ingreso > 2500000 and vivienda == 1 and estado_civil == 1:
      print('APROBADO')
    else:
      pass
      if ingreso > 3500000 and anos_banco >= 5:
        print('APROBADO')
      else:
        pass
        if vivienda == 2 and estado_civil == 2 and hijos < 2:
          print('APROBADO')
        else:
            print('RECHAZADO')