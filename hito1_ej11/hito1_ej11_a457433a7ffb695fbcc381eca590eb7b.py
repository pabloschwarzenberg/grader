saldo = 1000000
clave = 1803
usuario = 10334151
saldo_inicial = 100000
i=0
N = 2
op = 'N'
while op == 'N':
    usuario1 = int(input('Ingrese Usuario: '))
    clave1 = int(input('Ingrese clave: '))
    if clave1 == 1803:
        print('monto incial ' + str(saldo_inicial))
        a = int(input('Ingrese monto a retirar: '))
        if a <= 0 or a == saldo_inicial:
            print('monto no permitido')
        saldo_final = (saldo_inicial - a)
        print('saldo cuenta = ' + str(saldo_final))
        saldo_cajero = (saldo - a)
        print('saldo cajero = ' + str(saldo_cajero))
        billetes_20000 = 20
        w = a // 20000
        if w > 20:
            print('no hay dinero suficiente')
        print('billetes 20000=' + str(w))

        billetes_10000 = 40
        y = (a // 10000) - 2 * w
        if y > 40:
            print('no hay dinero suficiente')
        print('billetes 10000=' + str(y))

        billetes_5000 = 40
        z = (a // 5000) - (2*y+4*w)
        print('billetes 5000=' + str(z))



    else:
        print('clave invalida')
    op = input('para salir presione algo distinto a N para salir: ')
