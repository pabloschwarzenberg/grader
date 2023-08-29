#Aprobación de créditos
ingresos = int(input('Ingrese sus ingreso(en pesos) '))
ano_nacimiento = int(input('Ingrese su año de nacimiento '))
numero_hijos= int(input('Ingrese el número de hijos '))
ano_banco = int(input('Años de pertenencia al banco '))
estado_civil= input('Ingrese su estado civil ("S": soltero, "C", casado) ')
vive = input('Ingrese si vive en campo o cuidad ("U": urbano, "R": rural) ')

if ano_banco>10 and numero_hijos>=2:
  print('CREDITO APROBADO')
elif estado_civil=='C' and numero_hijos>=3 and ano_nacimiento in range(1968,1978):
  print('CREDITO APROBADO')
elif ingresos>2500000 and estado_civil=='S' and vive=='U':
  print('CREDITO APROBADO')
elif ingresos>3500000 and ano_banco>5:
  print('CREDITO APROBADO')
elif vive=='R' and estado_civil=='C' and numero_hijos<2:
  print('CREDITO APROBADO')
else:
  print('CREDITO NO APROBADO')      