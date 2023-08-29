#Cálculo del dígito verificador de un rut
rut = int(input())
suma = 0
n = 1


while rut != 0:
  m = rut % 10
  rut //= 10
  
  n += 1
  suma += m * n
  # print(m , n, suma)
  
  if n == 7:
    n = 1

resto = suma % 11

dv = 11 - resto

if dv == 11:
  dv = 0
elif dv == 10:
  dv = 'k'

print('dv={}'.format(dv))
