Num = int(input('ingrese el numero telefonico: '))
l = [0,1,2,3,4,5,7]
L = [8,9,10,11,12,13]
U = [14,15,16]
M = [17,18,19]
K = [20,21,22,23]

if 9999999<Num<99999999:
    hora = int(input('ingrese la hora de llamada: '))

    if hora == l[0] or hora == l[1] or hora == l[2] or hora == l[3] or hora == l[4] or hora == l[5] or hora == l[6]:
        print('CONTESTAR')

    if hora == L[0] or hora == L[1] or hora == L[2] or hora == L[3] or hora == L[4] or hora == L[5]:
        if Num%1000 == 909:
            print('CONTESTAR')
        else:
            hora == L[0] or hora == L[1] or hora == L[2] or hora == L[3] or hora == L[4] or hora == L[5]
            print('NO CONTESTAR')

    if hora == U[0] or hora == U[1] or hora == U[2]:
        print('NO CONTESTAR')

    if hora == M[0] or hora == M[1] or hora == M[2]:
        if Num//100000 != 877:
            print('CONTESTAR')
        else:
            Num//1000 == 877
            print('NO CONTESTAR')

    if hora == K[0] or hora == K[1] or hora == K[2] or hora == K[3]:
        print('NO CONTESTAR')
