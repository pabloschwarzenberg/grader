#Cajero Automático
usuario = int(input('ingresa número de usuario: '))
Saldo_Inicial = int(1000000)
opcion = "N"

if usuario == 10334151:
    monto = int(100000)
    i = 1
    clave = int(input('ingresa número de Clave: '))
    if clave != 1803:
        while i < 3 and clave != 1803:
            if i < 3:
                print('clave invalida')
                clave = int(input('ingresa número de clave: '))
                i = i + 1
            if i == 3:
                print('tarjeta bloqueada')
                break

    while opcion == 'N':
        sacaDinero = int(input('monto a retirar: '))
        while sacaDinero > monto:
            print('monto no permitido')
            sacaDinero = int(input('cuanto deseas retirar: '))

        monto = monto - sacaDinero
        Saldo_Inicial = Saldo_Inicial - sacaDinero
    
        print('saldo cuenta=', monto)
        print('saldo cajero=', Saldo_Inicial)
        opcion = input('¿deseas seguir retirando dinero?: ')