usuario = eval(input('ingresa numero de usuario: '))
clave = eval(input('ingresa clave: '))
saldocajero=1000000
saldocuenta=100000
cont = 0
while cont <= 3:
    if clave != 1803:
        cont = cont+1
        print('clave invalida')
        if cont == 3:
            print('tarjeta bloqueada')
    if usuario == 10334151 and clave == 1803:
        monto = eval(input('monto a retirar: '))
        if monto > saldocuenta:
            print('monto no permitido')
        elif monto <= saldocuenta:
            saldocuenta=saldocuenta-monto
            saldocajero=saldocajero-monto
            print('saldo cuenta: ', saldocuenta)
            print('saldo cajero: ', saldocajero)