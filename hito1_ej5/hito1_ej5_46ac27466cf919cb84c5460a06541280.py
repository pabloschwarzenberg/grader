#Cálculo del dígito verificador de un rut
rut = str(input('ingrese su rut'))
a = len(rut) - 1
b = 2
suma = 0
while a > -1:
  c = int(rut[a])
  num = c * b
  if b == 7:
    b = 1
  b += 1
  a -= 1
  suma += num
entero = suma//11
resto = suma - (11*entero)
dv = 11 - resto
if dv == 11:
  dv = 0
elif dv == 10:
  dv = 'k'
print('dv =', dv)