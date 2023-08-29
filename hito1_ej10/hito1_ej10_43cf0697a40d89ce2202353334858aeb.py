dinero_cliente=100000
intentos=0
dinero_cajero=1000000
persona = eval(input("Ingrese su Usuario:"))
if persona == 10334151:
    clave = eval(input("Ingrese su Clave:"))
    if clave == 1803:
            retirar_dinero = eval( input( "Cuanto desea retirar?" ) )
            if retirar_dinero <= 100000:
                saldo_cajero = dinero_cajero - retirar_dinero
                nuevo_saldo = dinero_cliente - retirar_dinero
                print( "monto permitido" )
                print( "saldo cuenta={}".format( nuevo_saldo ) )
                print( "saldo cajero={}".format( saldo_cajero ) )
            else:
                print( "monto no permitido" )
    else:
        while intentos < 2:
            print("clave invalida")
            clave=eval( input( "Ingrese su Clave:" ) )
            intentos += 1
        if clave == 1803:
            retirar_dinero = eval( input( "Cuanto desea retirar?" ) )
            if retirar_dinero <= 100000:
                saldo_cajero = dinero_cajero - retirar_dinero
                nuevo_saldo = dinero_cliente - retirar_dinero
                print( "monto permitido" )
                print( "saldo cuenta={}".format( nuevo_saldo ) )
                print( "saldo cajero={}".format( saldo_cajero ) )
            else:
                print( "monto no permitido" )
        elif intentos == 2:
            print("tarjeta bloqueada")  