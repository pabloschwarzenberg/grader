rut = int(input('Ingresa tu rut sin digito verificador: '))

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

print(d1, d2, d3, d4, d5, d6, d7, d8)

suma = d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2 + d8*3

print('suma: ', suma)

resto = suma%11
print('resto: ', resto)

resultado = 11 - resto

if resultado == 11:
    print('dv=0')

if resultado == 10:
    print('dv=K')

if resultado == 9:
    print('dv=9')

if resultado == 8:
    print('dv=8')

if resultado == 7:
    print('dv=7')

if resultado == 6:
    print('dv=6')

if resultado == 5:
    print('dv=5')

if resultado == 4:
    print('dv=4')

if resultado == 3:
    print('dv=3')

if resultado == 2:
    print('dv=2')

if resultado == 1:
    print('dv=1')
