ing=int(input('Ingreso(en pesos): '))
ano=int(input('Año de nacimiento: '))
hijos=int(input('Número de hijos: '))
anoB=int(input('Años de pertenencia al banco: '))
eciv=str.upper(input('Estado civil ("S": soltero, "C", casado): '))
viv=str.upper(input('Si vive en campo o cuidad ("U": urbano, "R": rural): '))
edad=2023-ano
if (anoB>=10 and hijos>=2):
  print('APROBADO')
elif (eciv=='C' and hijos>=3 and 45<= edad <=55):
  print('APROBADO')
elif (ing>=2500000 and eciv == 'S' and viv == 'C'):
  print('APROBADO')
elif (ing>=3500000 and anoB >= 5):
  print('APROBADO')
elif (viv == 'R' and eciv=='C' and hijos<=2):
  print('APROBADO')
else:
  print('RECHAZADO')