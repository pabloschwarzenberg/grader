#Aprobación de créditos
MONY=int(input('Ingreso (en pesos)'))
AN=int(input('Año de nacimiento'))
NH=int(input('Número de hijos'))
AB=int(input('Años de pertenencia al banco'))
ES=(input('Estado civil ("S": soltero, "C", casado)'))
VV=(input('Locación Vivienda ("U": urbano, "R": rural)'))
ANO=int(2020-AN)
if AB > 10 and NH >= 2 :
  print('APROBADO')
elif ES == 'C' and NH >= 3 and ANO >= 45 and ANO <= 55 :
  print('APROBADO')
elif MONY < 2500000 and ES == 'S' and VV == 'U' :
  print('APROBADO')
elif MONY < 3500000 and AB > 5 :
  print('APROBADO')
elif VV == 'R' and ES == 'C' and NH < 2 :
  print('APROBADO')
else:
  print('RECHAZADO')
