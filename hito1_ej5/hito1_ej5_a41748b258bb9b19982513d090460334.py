#Cálculo del dígito verificador de un rut
rut = float(input('Ingrese su rut sin el dígito verificador, y el prográma se lo calculará: '))
N8 = ((rut // 1) % 10) * 2
N7 = ((rut // 10) % 10) * 3
N6 = ((rut // 100) % 10) * 4
N5 = ((rut // 1000) % 10) * 5
N4 = ((rut // 10000) % 10) * 6
N3 = ((rut // 100000) % 10) * 7
N2 = ((rut // 1000000) % 10) * 2
N1 = ((rut // 10000000) % 10) * 3
S = N1 + N2 + N3 + N4 + N5 + N6 + N7 + N8
Mod11 = S % 11
F = 11 - Mod11
if F == 11:
    print('dv = 0')
if F == 10:
    print('dv = k')
else:
    print('dv =', F)