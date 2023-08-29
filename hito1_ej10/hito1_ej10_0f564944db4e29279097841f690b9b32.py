#Cajero Automático
monto_cajero=1000000
monto_usuario=100000
clave_invalida=0
while True:
    usuario=int(input('Ingrese numero de Usuario:'))
    clave=int(input('Ingrese Clave:'))
    if clave==1803 and usuario==10334151:
        monto_retirar=int(input('Ingrese monto a retirar:'))
        if monto_retirar<=100000:
            if monto_usuario>=monto_retirar and monto_usuario>0:
                print('Se retira:',monto_retirar)
                monto_cajero=monto_cajero-monto_retirar
                monto_usuario=monto_usuario-monto_retirar
                print('saldo cuenta=',monto_usuario)
                print('saldo cajero=',monto_cajero)
                salir=input('Desea salir(Digite N para continuar):')
                salir=salir.upper()
                if salir=="N":
                    continue
                else:
                    break
            else:
                print('No hay saldo suficiente')     
        else:
            print('monto no permitido')
    elif clave!=1803:
        print('clave invalida')
        clave_invalida=clave_invalida+1
        if clave_invalida==3:
            print('tarjeta bloqueada')
            break
        else:
            continue
    else:
        break