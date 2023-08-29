#Cálculo del dígito verificador de un rut
rut = input('Ingrese rut: ')
rut = rut[::-1]

digit_sum = 0
multiplier = 2
for digit in rut:
  digit_sum += (int(digit) * multiplier)
  if multiplier < 7:
    multiplier += 1
  else:
    multiplier = 2

verificator = 11 - (digit_sum % 11)

if verificator == 11:
  verificator = 0
elif verificator == 10:
  verificator = 'K'

print('dv=', verificator)
