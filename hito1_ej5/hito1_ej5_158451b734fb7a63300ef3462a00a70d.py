#Cálculo del dígito verificador de un rut
rut = input('Ingresa RUT sin dv: ')
largo = len(rut)
multi = 1
suma = 0
for i in range(largo-1,-1,-1):
    multi = multi + 1
    suma = suma + int(rut[i])*multi
    if multi == 7:
        multi = 1
resto = suma % 11
dv = 11 - resto
dv = str(dv)
if dv == '11':
    dv = '0'
if dv == '10':
    dv = 'K'
print('dv=',dv)