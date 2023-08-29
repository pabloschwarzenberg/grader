#Cálculo del dígito verificador de un rut
rut = input('Ingrese rut sin dígito verificador: ')

largo = len(rut)

contador = 1
sumador = 0
for x in range(largo-1, -1, -1):
    
    contador = contador + 1
    sumador = sumador + int(rut[x])*contador
    if contador == 7:
        contador = 1
resto = sumador%11

dv = 11 - resto

if dv == 11:
    dv = 0
elif dv == 10:
    dv = 'k'
    

print('dv=', dv)