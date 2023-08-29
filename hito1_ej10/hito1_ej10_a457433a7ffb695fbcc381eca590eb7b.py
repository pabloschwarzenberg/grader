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
    else:
        print('clave invalida')
    op = input('para salir presione algo distinto a N para salir: ')
