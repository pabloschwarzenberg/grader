#Cajero Automático
usuario = int(input('Ingrese su usuario: '))
clave = int(input('Ingrese su clave: '))
saldo_cajero = 1000000
saldo_cuanta = 100000

if clave != 1803:
    print('clave invalida')
    clave = int(input('Ingrese su clave: '))
    if clave != 1803:
        print('clave invalida')
        clave = int(input('Ingrese su clave: '))
        if clave != 1803:
            print('tarjeta bloqueada')
if clave == 1803:
    retiro = int(input('Ingrese el monto a retirar: '))
    if retiro > saldo_cuanta:
        print('monto no permitido')
        retiro = int(input('Ingrese el monto a retirar: '))
    if retiro < saldo_cuanta:
        total = saldo_cuanta - retiro
        cajero = saldo_cajero - retiro
        print('saldo cuenta=',total,)
        print('saldo cajero=',cajero,)