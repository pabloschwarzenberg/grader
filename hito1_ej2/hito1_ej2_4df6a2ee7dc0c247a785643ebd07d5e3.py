#Contestador de celular
num = int(input('ingrese un numero telefonico: '))
a = [0,1,2,3,4,5,7]
s = [8,9,10,11,12,13]
d = [14,15,16]
f = [17,18,19]
g = [20,21,22,23]
if 9999999 < num < 99999999:
    hora = int(input('ingrese la hora de la llamada: '))
    if hora == a[0] or hora == a[1] or hora == a[2] or hora == a[3] or hora == a[4] or hora == a[5] or hora == a[6]:
        print('contestar')
    if hora == s[0] or hora == s[1] or hora == s[2] or hora == s[3] or hora == s[4] or hora == s[5]:
        if num % 1000 == 909:
            print('contestar')
        else:
            hora == s[0] or hora == s[1] or hora == s[2] or hora == s[3] or hora == s[4] or hora == s[5]
            print('no contestar')
    if hora == d[0] or hora == d[1] or hora == d[2]:
        print('no contestar')
    if hora == f[0] or hora == f[1] or hora == f[2]:
        if num//100000 != 877:
            print('contestar')
        else:
            num // 1000 == 877
            print('no contestar')
    if hora == g[0] or hora == g[1] or hora == g[2] or hora == g[3]:
        print('no contestar')