#Cajero Automático
usuario=input('Ingresa tu número de usuario: ')
def cajero_automatico(usuario):
    intento=0
    saldocajero=1000000
    saldocuenta=100000
    clave=0
    billetes_20000=20
    billetes_10000=40
    billetes_5000=40
    billetes20=0
    billetes10=0
    billetes5=0
    clave=eval(input('Ingresa tu clave: '))
    while clave!=1803:
        intento=intento+1
        if intento==1 or intento==2:
            print('clave invalida')
        if intento==3 and clave!=1803:
            print('tarjeta bloqueada')
            break
        clave=eval(input('Ingresa tu clave: '))
    if clave==1803:
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
            billetes20=retiro//20000
            retiro=retiro-(billetes20)*20000
            billetes10=retiro//10000
            retiro=retiro-(billetes10)*10000
            billetes5=retiro//5000
            print('billetes 20000=',billetes20)
            print('billetes 10000=',billetes10)
            print('billetes 5000=',billetes5)
cajero_automatico(usuario)
