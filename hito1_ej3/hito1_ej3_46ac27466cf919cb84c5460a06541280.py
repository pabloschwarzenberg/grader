#Aprobación de créditos
ingresos = int(input('Ingresos del usuario'))   
nacimiento = int(input('Ingrese su año de nacimiento'))
hijosnum = int(input('Ingrese la cantidad de hijos que tenga'))
bancopertenencia = int(input('Ingrese los Años de pertenencia al banco'))
estadocivil = str(input('"S": soltero, "C": casado'))
vivienda = str(input('"U": urbano, "R": rural'))
if (bancopertenencia > 10) and (hijosnum >= 2):
  print('APROBADO')
elif (estadocivil == 'C') and (hijosnum > 3) and (nacimiento >= 45) and (nacimiento <= 55):
  print('APROBADO')
elif (ingresos > 2500000) and (estadocivil == 'S') and (vivienda == 'U'):
  print('APROBADO')
elif (ingresos > 3500000) and (bancopertenencia > 5):
  print('APROBADO')
elif (vivienda == 'R') and (estadocivil == 'C') and (hijosnum < 2):
  print('APROBADO')
print('RECHAZADO')