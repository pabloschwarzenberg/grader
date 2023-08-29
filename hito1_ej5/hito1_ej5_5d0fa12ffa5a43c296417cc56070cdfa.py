rut = input('ingrese el rut: ')

largo = len(rut)
multiplo = 1
sumador = 0

for x in range(largo-1,-1,-1):
    multiplo = multiplo+1
    resultado = (int(rut[x])*multiplo)
    sumador = sumador+resultado

    if(multiplo==7):
        multiplo=1

resto = sumador%11

a = range(resto)

DV = 11-resto

if(DV ==11):
    DV = '0'
if(DV ==10):
    DV = 'K'

print('dv=', DV)