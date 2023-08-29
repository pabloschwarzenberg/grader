#Aprobación de créditos
ingreso = int(input('Ingreso (en pesos): '))
ano = int(input('Ano de nacimiento: '))
edad = 2020-ano
numHijos = int(input('Numero de hijos: '))
anosBanco = int(input('Anos de pertenencia al banco: '))
eCivil = input('Estado civil ("S": soltero, "C", casado): ')
sector = input('Sector ("U": urbano, "R": rural): ')
if ((anosBanco > 10) and (numHijos >= 2)):
  print('APROBADO')
elif ((eCivil == 'C') and (numHijos > 3) and ((edad >=45) and (edad <= 55))):
  print('APROBADO')
elif ((ingreso > 2500000) and (eCivil == 'S') and (sector == 'R')):
  print('APROBADO')
elif ((ingreso > 3500000) and (anosBanco > 5)):
  print('APROBADO')
elif ((sector == 'U') and (eCivil == 'C') and (numHijos < 2)):
  print('APROBADO')
else:
  print('RECHAZADO')     