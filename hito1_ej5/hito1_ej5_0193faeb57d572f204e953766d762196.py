#Cálculo del dígito verificador de un rut
rut = int(input('Ingresa tu RUT sin dígito verificador: '))

d1 = rut%10
rut = rut//10

d2 = rut%10
rut = rut//10

d3 = rut%10
rut = rut//10

d4 = rut%10
rut = rut//10

d5 = rut%10
rut = rut//10

d6 = rut%10
rut = rut//10

d7 = rut%10
rut = rut//10

d8 = rut%10
rut = rut//10

suma = d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2 + d8*3

resto = suma%11

resultado = 11 - resto

if resultado == 11:
    print('dv=0')

if resultado == 10:
    print('dv=K')

if resultado != 11 and resultado != 10:
    print('dv=', resultado)     