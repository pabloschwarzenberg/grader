#Aprobación de créditos
ingreso=int(input('ingrese el monto'))
fecha=int(input('ingrese el año de nacimiento'))
hijos=int(input('ingrese el numero de hijos'))
anosbanco=int(input('ingrese cuantos años pertenece al banco'))
estadocivil=input('si es soltero S,casado C')
vivienda=input('si vive en urbano U,rural R')
if anosbanco>10 and hijos>=2:
      print('APROBADO')
elif estadocivil == 'C' and hijos>3 and(1975>=fecha>=1965):
      print('APROBADO')
elif ingreso>2500000 and estadocivil== 'S' and anosbanco >5:
      print('APROBADO')
elif ingreso>3500000 and anosbanco>5:
      print('APROBADO')
elif vivienda == 'R' and estadocivil== 'C' and hijos<2:
      print('APROBADO')
else:
      print('RECHAZADO')
      