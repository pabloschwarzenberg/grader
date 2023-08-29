#Cálculo del dígito verificador de un rut
ruts = input('\nintroduzca su rut sin digito verificador:')
p2 = ''
largo = len(ruts) - 1
suma = 0
factor = 2
while largo >= 0:
    p2 += ruts[largo]
    largo -= 1
for num in p2:
    suma += int(num) * factor
    factor = 2 if factor == 7 else factor + 1
resto = suma % 11
dv = 11 - resto
if dv < 10:
    dv = dv
elif dv == 10:
    dv = 'k'
else:
    dv = 0
print('dv={}'.format(dv))      