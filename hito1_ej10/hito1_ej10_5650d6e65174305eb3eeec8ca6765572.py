usuario=int(input('Ingresa el usuario: '))
clave=int(input('Ingresa tu clave: '))
saldo_cajero=1000000

i=0
while i<=3:
    if usuario==10334151 and clave==1803:
        saldo_usuario=100000
        retiro=int(input('Ingresa el monto que quieres retirar: '))

        if retiro<=saldo_usuario:
             saldo_usuario=saldo_usuario-retiro
             saldo_cajero=saldo_cajero-retiro
             print('saldo cuenta=',saldo_usuario,'saldo cajero=',saldo_cajero)
             break
        else:
            print('monto no permitido')
            break

    else:
        if i<=3:
            i=i+1
            print('clave invalida')
        else:
            print('tarjeta bloqueada')
            break
