#Cálculo del dígito verificador de un 
print('**Calcular digito verificador**')
rut = str(input('Ingrese su RUT: '))
n1 = int(rut[0:1])
n2 = int(rut[1:2])
n3 = int(rut[2:3])
n4 = int(rut[3:4])
n5 = int(rut[4:5])
n6 = int(rut[5:6])
n7 = int(rut[6:7])

if (len(rut) == 7):
  sumaProductos = (n7*2)+(n6*3)+(n5*4)+(n4*5)+(n3*6)+(n2*7)+(n1*2)
  division = sumaProductos/11
  resta = sumaProductos - (11 * int(division))
  final = int(11 - resta)
  if (final == 11):
    dv = 0
  elif (final == 10):
    dv = 'K'
  else:
    dv = final
  print('dv='+str(dv))
elif (len(rut) == 8):
  n8 = int(rut[7:8])
  sumaProductos = (n8*2)+(n7*3)+(n6*4)+(n5*5)+(n4*6)+(n3*7)+(n2*2)+(n1*3)
  division = sumaProductos/11
  resta = sumaProductos - (11 * int(division))
  final = int(11 - resta)
  if (final == 11):
    dv = 0
  elif (final == 10):
    dv = 'K'
  else:
    dv = final
  print('dv='+str(dv))
else:
  print('RUT Incorrecto')