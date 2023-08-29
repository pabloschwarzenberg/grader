saldo_cajero=1000000
saldo_cuenta=100000
while True:
    validation=str(input('disto a N para salir: '))
    validation=validation.upper()
    if validation!='N':
        break
    user=str(input('Ingrese usuario: '))
    if user!='10334151':
        print('Usuario no valido')
    else:
        intentos=0
        while intentos<3:
            clave=int(input('Ingrese Clave: '))
            if clave==1803:
                break
        intentos=intentos+1
        if intentos==3:
            print('tarjeta bloqueada')
            break
        else:
            Retiro=int(input('Ingrese monto a retirar: '))
            if Retiro>1000000 or Retiro>100000:
                print('monto no permitido')
            else:
                saldo_cuenta=saldo_cuenta-Retiro
                saldo_cajero=saldo_cajero-Retiro
                print('saldo cuenta=',saldo_cuenta+str(saldo_cuenta)+str(' saldo cajero=')+str(saldo_cajero))