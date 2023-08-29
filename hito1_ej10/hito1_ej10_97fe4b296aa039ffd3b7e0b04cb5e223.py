#Cajero Automático
usuario=input('Ingresa tu número de usuario: ')
def cajero_automatico(usuario):
    intento=0
    saldocajero=1000000
    saldocuenta=100000
    clave=0
    clave=eval(input('Ingresa tu clave: '))
    while clave!=1803:
        intento=intento+1
        if intento==1 or intento==2:
            print('clave invalida')
        if intento==3 and clave!=1803:
            print('tarjeta bloqueada')
            break
        clave=eval(input('Ingresa tu clave: '))
    retiro=int(input('monto a retirar: '))
    while 0>retiro or retiro>saldocuenta:
        if 0>retiro or retiro>saldocuenta:
            print ('monto no permitido')
            retiro=int(input('monto a retirar: '))
    if 0<retiro<=saldocuenta:
        saldocuenta-=retiro
        saldocajero-=retiro
        print('saldo cuenta=',saldocuenta)
        print('saldo cajero=',saldocajero)
cajero_automatico(usuario)   