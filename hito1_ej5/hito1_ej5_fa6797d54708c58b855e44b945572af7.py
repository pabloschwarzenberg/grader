rut = int(input('Ingresa tu RUT: '))

n1 = rut%10
n2 = rut%100//10
n3 = rut%1000//100
n4 = rut//1000%10
n5 = rut//10000%10
n6 = rut//100000%10
n7 = rut//1000000%10
n8 = rut//10000000

resultado = (n1*2 + n2*3 + n3*4 + n4*5 + n5*6 + n6*7 + n7*2 + n8*3)

resto = resultado%11

dv = 11 - resto
if rut >= 10000000 and rut <= 99999999:
    if dv >= 1 and dv <= 9:
        print('dv= ', dv,)

    if dv == 11:
        print('dv= 0')

    if dv == 10:
        print('dv= K')

resultado = (n1*2 + n2*3 + n3*4 + n4*5 + n5*6 + n6*7 + n7*2)
if rut >= 1000000 and rut <= 9999999:
    if dv >= 1 and dv <= 9:
        print('dv= ', dv,)

    if dv == 11:
        print('dv= 0')

    if dv == 10:
        print('dv= K')
