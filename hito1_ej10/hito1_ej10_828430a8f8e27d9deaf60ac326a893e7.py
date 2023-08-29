intentos = 0
condicion_clave = True
saldo_incial = 1000000
usuario = 10334151
clave_usuario = 1803
cuenta_usuario = 100000

'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
while condicion_clave:
    clave_ingresada = eval(input('ingrese su clave: '))
    if clave_usuario != clave_ingresada:
        intentos = intentos+1
        print('clave invalida')
    if intentos == 3:
        print('tarjeta bloqueada')
        condicion_clave = False
    if clave_ingresada == clave_usuario:
        retirando = eval(input('Ingrese el monto que desea retirar: '))
        if retirando > cuenta_usuario or retirando > saldo_incial:
            print('monto no permitido')
        else:
            saldo_incial = saldo_incial - retirando
            cuenta_usuario = cuenta_usuario - retirando
            print('saldo cuenta=',cuenta_usuario)
            print('saldo cajero=',saldo_incial)
