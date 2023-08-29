#Cálculo del dígito verificador de un rut
rut = input('Ingrese RUT: ') #19.688.260

if int(rut)>= 10000000:
  a = int(rut[7:])
  b = int(rut[6:7])
  c = int(rut[5:6])
  d = int(rut[4:5])
  e = int(rut[3:4])
  f = int(rut[2:3])
  g = int(rut[1:2])
  h = int(rut[:1])
  suma = (a*9)+(b*8)+(c*7)+(d*6)+(e*5)+(f*4)+(g*9)+(h*8)
  resto = suma%11
  if resto != 10:
      print('dv = ',resto)
  else:
      print('dv = k')

elif int(rut)<= 10000000:
    b = int(rut[6:])
    c = int(rut[5:6])
    d = int(rut[4:5])
    e = int(rut[3:4])
    f = int(rut[2:3])
    g = int(rut[1:2])
    h = int(rut[:1])
    suma = (b*9)+(c*8)+(d*7)+(e*6)+(f*5)+(g*4)+(h*9)
    resto = suma%11
    if resto != 10:
      print('dv = ',resto)
    else:
      print('dv = k')
