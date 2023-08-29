#Contestador de celular
num = int(input('ingrese un numero de telefono: '))
a = [0,1,2,3,4,5,7]
b = [8,9,10,11,12,13]
c = [14,15,16]
f = [17,18,19]
g = [20,21,22,23]
if 9999999 < num < 99999999:
    hora = int(input('ingrese la hora de la llamada: '))
    if hora == a[0] or hora == a[1] or hora == a[2] or hora == a[3] or hora == a[4] or hora == a[5] or hora == a[6]:
        print('contestar')
    if hora == b[0] or hora == b[1] or hora == b[2] or hora == b[3] or hora == b[4] or hora == b[5]:
        if num % 1000 == 909:
            print('contestar')
        else:
            hora == b[0] or hora == b[1] or hora == b[2] or hora == b[3] or hora == b[4] or hora == b[5]
            print('no contestar')
    if hora == c[0] or hora == c[1] or hora == c[2]:
        print('no contestar')
    if hora == f[0] or hora == f[1] or hora == f[2]:
        if num//100000 != 877:
            print('contestar')
        else:
            num // 1000 == 877
            print('no contestar')
    if hora == g[0] or hora == g[1] or hora == g[2] or hora == g[3]:
        print('no contestar')      