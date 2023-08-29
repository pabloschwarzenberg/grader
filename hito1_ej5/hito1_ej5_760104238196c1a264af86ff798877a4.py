#Cálculo del dígito verificador de un rut
x = input()
numeros = []
for i in x:
  numeros.insert(0,int(i))
suma = 0
n = 0
for i in numeros:
  suma += i * (n % 6 + 2)
  n += 1
dv = (11 - suma%11)%11
if dv == 10:
  dv = 'K'
else:
  dv = str(dv)
print('dv=' + dv)
