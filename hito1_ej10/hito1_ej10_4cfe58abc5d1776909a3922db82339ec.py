#Cajero Automático
scaj = 1000000
funca = 1
uid1 = 10334151
pass1 = 1803
monto1 = 100000
logscr = 1
attempt = 0
while funca == 1:
    if logscr == 1:
        logid = int(input('Ingresar numero de usuario: '))
        logpass = int(input('Ingrese clave: '))
        if (logid == uid1) and (logpass == pass1):
            logscr = 2
        else:
            attempt += 1
            print ('clave invalida')
            if attempt >= 3:
                print ('tarjeta bloqueada')
                funca = 0
    if logscr == 2:
        giro = int(input('Monto a retirar: '))
        if (giro > monto1) or (giro > scaj):
            print('monto no permitido')
        else:
            monto1 -= giro
            scaj -= giro
            print('saldo cuenta=', monto1)
            print('saldo cajero=', scaj)
            opc = input('presione N para volver a girar, para salir del programa, cualquier otra tecla: ')
            if (opc == 'N'):
                logscr = 2
            else:
                funca = 0
else:
    print('fin')      