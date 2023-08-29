#Aprobación de créditos
ingreso = int(input())
edad = 2018 - int(input())
hijos = int(input())
ano_pertenencia = int(input())
estado_civil = input()
vivienda = input()

if ano_pertenencia > 10 and hijos >= 2:
  print('APROBADO')
elif estado_civil == 'C' and hijos > 3 and 45 <= edad <= 55:
  print('APROBADO')
elif ingreso > 2500000 and estado_civil == 'S' and vivienda == 'U':
  print('APROBADO')
elif ingreso > 3500000 and ano_pertenencia > 5:
  print('APROBADO')
elif vivienda == 'R' and estado_civil == 'C' and hijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')