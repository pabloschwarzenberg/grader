#Aprobación de créditos
# entrada
a = int(input('ingrese el monto que desea declarar: '))
b = int(input('ingrese su año de nacimiento: '))
c = int(input('ingrese cuantos hijos tiene: '))
d = int(input('cuantos años lleva inscrito al banco?: '))
e = str(input('declare su estado civil (S/C): '))
f = str(input('vive en un lugar Urbano o Rural? (U/R): '))
periodo = 2021

# procesamiento
if (a >= 2500000) and (e == 'S') and (f == 'U'):
  print('APROBADO')
elif (a >= 3500000) and (d >= 5):
  print('APROBADO')
elif (f == 'R') and (e == 'C') and (c <= 2):
  print('APROBADO')
elif (e == 'C') and (c >= 3) and (periodo - a >= 45 <= 55):
  print('APROBADO')
elif (a >= 10) and (c >= 2):
  print('APROBADO')
else:
  print('RECHAZADO')
