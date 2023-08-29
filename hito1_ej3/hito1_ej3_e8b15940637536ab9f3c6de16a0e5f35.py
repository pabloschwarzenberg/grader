#Aprobación de créditos

ingreso = int(input('Ingrese de cuanto es su ingreso (en pesos,):'))
año = int(input('Ingrese año de nacimiento:'))
ndehijos = int(input('Ingrese su número de hijos:'))
tiempo = int(input('Ingrese sus años de pertenencia al banco:'))
estado = str(input('Defina sus estado civil "S": soltero, "C", casado:'))
vivienda = str(input('Defina si vive en campo o cuidad "U": urbano, "R": rural:'))
edad = 2020 - año
if tiempo > 10 and ndehijos > 2:
  print ('APROBADO')
elif estado == 'c' and ndehijos > 3 and 45<=edad<=55:
  print ('APROBADO')
elif ingreso > 2500000 and estado == 's' and vivienda == 'U':
  print ('APROBADO')
elif ingreso > 3500000 and tiempo > 5:
 print ('APROBADO')
elif vivienda == 'R' and estado == 's' and ndehijos < 2:
  print ('APROBADO')
else:
  print ('DESAPROBADO')