#Contestador de celular
numero = int(input('ingrese el numero telefonico: '))
l = [0,1,2,3,4,5,7]
L = [8,9,10,11,12,13]
i = [14,15,16]
n = [17,18,19]
k = [20,21,22,23]

if 9999999<numero<99999999:
    hora = int(input('ingrese la hora de llamada: '))

    if hora == l[0] or hora == l[1] or hora == l[2] or hora == l[3] or hora == l[4] or hora == l[5] or hora == l[6]:
        print('contestar')

    if hora == L[0] or hora == L[1] or hora == L[2] or hora == L[3] or hora == L[4] or hora == L[5]:
        if numero%1000 == 909:
            print('contestar')
        else:
            hora == L[0] or hora == L[1] or hora == L[2] or hora == L[3] or hora == L[4] or hora == L[5]
            print('no contestar')

    if hora == i[0] or hora == i[1] or hora == i[2]:
        print('no contestar')

    if hora == n[0] or hora == n[1] or hora == n[2]:
        if numero//100000 != 877:
            print('contestar')
        else:
            numero//1000 == 877
            print('no contestar')

    if hora == k[0] or hora == k[1] or hora == k[2] or hora == k[3]:
        print('no contestar')      