rut = input('Ingrese el número de RUT sin dígito verificador: ')

factor = 2
suma = 0

for digito in reversed(rut):
    suma = suma + int(digito) * factor
    factor = factor + 1
    if factor == 8:
        factor = 2

dv = 11 - (suma % 11)

if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'K'

print('dv =', dv)

      