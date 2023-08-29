num_1 = str(input('Ingrese su RUT sin dv: '))
if len(num_1) == 8:
    a = int(num_1[0]) * 3
    b = int(num_1[1]) * 2
    c = int(num_1[2]) * 7
    d = int(num_1[3]) * 6
    e = int(num_1[4]) * 5
    f = int(num_1[5]) * 4
    g = int(num_1[6]) * 3
    h = int(num_1[7]) * 2
    suma = a + b + c + d + e + f + g + h
elif len(num_1) == 7:
    a = int(num_1[0]) * 2
    b = int(num_1[1]) * 7
    c = int(num_1[2]) * 6
    d = int(num_1[3]) * 5
    e = int(num_1[4]) * 4
    f = int(num_1[5]) * 3
    g = int(num_1[6]) * 2
    suma = a + b + c + d + e + f + g
div = suma // 11
div_0 = suma - (11 * div)
div_1 = 11 - div_0
if div_1 == 11:
    print('dv = 0')
elif div_1 == 10:
    print('dv = k')
elif div_1 < 10:
    print('dv =', div_1)

