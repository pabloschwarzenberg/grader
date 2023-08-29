combinacion=[int(input('Ingreso (en pesos): ')),int(input('Año de nacimiento: ')),int(input('Número de hijos: ')),int(input('Años de pertenencia al banco: ')),input('Estado Civil:  ("S": soltero, "C", casado): '),input('Si vive en campo o cuidad ("U": urbano, "R": rural): ')]
Ingreso=int(combinacion[0])
Año=int(combinacion[1])
hijos=int(combinacion[2])
pertenencia=int(combinacion[3])
Estado=combinacion[4]
residencia=combinacion[5]
if pertenencia>10 and hijos>=2:
  print('APROBADO')
elif Estado=='C' and hijos>3 and 45>=(2021-Año)<=55:
  print('APROBADO')
elif Ingreso>=2500000 and Estado=='S' and residencia=='U':
  print('APROBADO')
elif Ingreso>=3500000 and pertenencia>=5:
  print('APROBADO')
elif residencia=='R' and Estado=='C'and hijos<=2:
  print('APROBADO')
else:
  print('RECHAZADO')
