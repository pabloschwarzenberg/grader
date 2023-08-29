#Aprobación de créditos
ingreso = int(input('Cuanto es su ingreso: '))
año = int(input('Edad: '))
hijos = int(input('Cuantos hijos tiene: '))
añosbanco = int(input('Cuantos años lleva pertenenciendo al banco: '))
estado = input('Estado civil("S": soltero, "C":casado): ')
vive = input('Donde vive("U": urbano, "R": rural): ')

año = 2020 - año


if añosbanco > 10 and hijos >= 2:
  print('APROBADO')
elif estado == 'C' and hijos > 3 and 45 <= año <= 55:
  print('APROBADO')
elif ingreso > 250000 and estado == 'S' and vive == 'U':
  print('APROBADO')
elif ingreso > 350000 and añosbanco > 5:
  print('APROBADO')
elif vive == 'R' and estado == 'C' and hijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')       