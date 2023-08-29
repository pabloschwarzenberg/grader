#Aprobación de créditos
Ing=int(input('Ingrso'))
nac= int(input('Año de nacimiento'))
hij=int(input('cant hijos'))
pbanco=int(input('Ingreso al banco'))
EC=input('Estado civil')
Viv=input('Rural o Urbano')
edad= 2023 - nac
if pbanco> 10 and hij>=2:
  print('APROBADO')
elif EC=='C'and hij>3 and(edad>=45 and edad<=55):
  print('APROBADO')
elif Ing>2500000 and EC=='S'and Viv =='U':
  print('APROBADO')
elif Ing>3500000 and pbanco> 5:
  print('APROBADO')
elif Viv =='R' and EC== 'C' and hij<2:
  print('APROBADO')
else:
  print('RECHAZADO')
