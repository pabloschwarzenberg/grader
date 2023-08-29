#Aprobación de créditos
ingreso = int(input())
nacimiento = int(input())
hijos = int(input())
pertenencia = int(input())
civil = input()
residencia = input()

a = (hijos >= 2) and (pertenencia > 10)
b = (civil == 'C') and (hijos > 3) and (2022 - 55 <= nacimiento <= 2022 - 45)
c = (ingreso > 2500000) and (civil == 'S') and (residencia == 'U')
d = (ingreso > 3500000) and (pertenencia > 5)
e = (residencia == 'R') and (civil == 'C') and (hijos < 2)

if a or b or c or d or e:
  print('APROBADO')
else:
  print('RECHAZADO')
