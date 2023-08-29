#Cálculo del dígito verificador de un rut
num = int(input('Ingrese su rut: '))
x = [int(i) for i in str(num)]
x.reverse()
z = len(x)

if z == 8:
    k = x[0] * 2
    k1 = x[1] * 3
    k2 = x[2] * 4
    k3 = x[3] * 5
    k4 = x[4] * 6
    k5 = x[5] * 7
    k6 = x[6] * 2
    k7 = x[7] * 3
    suma = k + k1+ k2 + k3 + k4 + k5 + k6 + k7
    div = suma % 11
    resta = 11 - div
    if resta == 11:
        print('dv=0')
    elif resta == 10:
        print('dv=K')
    else:
        print('dv=',resta,)
elif z == 7:
    k = x[0] * 2
    k1 = x[1] * 3
    k2 = x[2] * 4
    k3 = x[3] * 5
    k4 = x[4] * 6
    k5 = x[5] * 7
    k6 = x[6] * 2
    suma = k + k1+ k2 + k3 + k4 + k5 + k6
    div = suma % 11
    resta = 11 - div
    if resta == 11:
        print('dv=0')
    elif resta == 10:
        print('dv=K')
    else:
        print('dv=',resta,)


    