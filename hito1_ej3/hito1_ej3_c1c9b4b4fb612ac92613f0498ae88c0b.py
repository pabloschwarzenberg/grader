#Aprobación de créditos
import time
A=int(time.strftime('%Y'))
pesos=round(float(input('ingreso del cliente (en pesos)')))
AN=int(float(input('ingrese año de nacimiento (con 4 digitos: xxxx)')))
hijos=int(float(input('cuantos hijos tiene')))
AP=int(float(input('¿cuantos años a pertenecido al banco?')))
estadoC=input('ingrese estado civil(S:soltero, C:casado)')
vivienda=input('ingrese tipo de vivienda(U:ciudad, R:rural)')
edad=A-AN
if AP>10 and hijos>=2:
  print('APROBADO')
elif estadoC=='C' and hijos>3 and edad in range(45,50):
  print('APROBADO')
elif pesos>2500000 and estadoC=='S' and vivienda=='U':
  print('APROBADO')
elif pesos>3500000 and AP>5:
  print('APROBADO')
elif vivienda=='R' and estadoC=='C' and hijos<2:
  print('APROBADO')
else:
  print('RECHAZADO')