#Cajero Automático
bloq = False
clave = 1803
N = ''
xd = ''
d_cajero = 1000000
d_usuario = 100000
b20k = 0
b10k = 0
b5k = 0
con = 1

while xd == N:
    u = str(input('usuario: '))
    c = int(input('clave: '))
    while c != clave and con != 3:
        print('calve invalida')
        u = str(input('usuario: '))
        c = int(input('clave: '))
        con = con + 1
        if con == 3 and clave != c:
            bloq = True

    if bloq == False:
        if  c == clave:
            monto = int(input('Ingrese monto: '))
            while monto > d_cajero or monto < 0:
                print('monto no permitido')
                monto = int(input('Ingrese monto: '))
            s_cajero = d_cajero - monto
            s_usuario = d_usuario -monto
            cum = monto

            while cum >= 20000:
                b20k = (int(monto/20000) + b20k)
                monto = b20k
                cum = cum - 20000


            while cum >= 10000:
                monto = cum
                b10k = (int(monto/10000) + b10k)
                monto = b10k
                cum = cum - 10000


            while cum >= 5000:
                monto = cum
                b5k = (int(monto/5000) + b5k)
                monto = b5k
                cum = cum - 5000




            print('saldo cajero={}'.format(s_cajero))
            print('saldo cuenta={}'.format(s_usuario))
            print('billetes 20000=',b20k)
            print('billetes 10000=',b10k)
            print('billetes 5000=',b5k)
            
            xd = str(input('Para salir ingrese algo distinto a N: '))
        
    if bloq == True:
        print('tarjeta bloqueada')
