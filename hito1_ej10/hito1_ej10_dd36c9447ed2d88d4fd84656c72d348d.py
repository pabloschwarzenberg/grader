cajero=1000000
cuenta=100000
contador=0
usuario=input('ingrese usuario: ')
while contador<3:
    clave=input('ingrese contraseña: ')
    if usuario!='10334151' and clave!='1803':
        contador=contador+1
        print('usuario o clave incorrecto')
    elif usuario=='10334151' and clave=='1803':
        monto=int(input('monto a retirar: '))
        if monto>100000:
            print('monto no permitido')
        elif monto<1000000:
            cajero=cajero-monto
            cuenta=cuenta-monto
            print ("saldo cuenta=",cuenta)
            print("saldo cajero=",cajero)
            break
    else:
        contador=contador+1
        print('tarjeta bloqueada')

