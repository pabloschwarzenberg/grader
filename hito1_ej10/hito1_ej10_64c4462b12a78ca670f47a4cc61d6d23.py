#Cajero Automático

usuario = int(input('usuario'))
clave = int(input('clave'))
monto_cajero = 1000000
monto_usuario = 100000
intentos = 3

while True:
    while intentos > 0:
        if usuario == 10334151 and clave == 1803:
            retiro = int(input('monto a retirar'))
            if retiro > monto_usuario:
                print('monto no permitido')
            else:
                monto_cajero -= retiro
                monto_usuario -= retiro
                print('saldo cuenta =', monto_usuario)
                print('saldo cajero =', monto_cajero)
        elif intentos > 0:
            intentos -= 3
            print('clave invalida')
        else:
            print('tarjeta bloqueada')
    a = input()
    if input != N:
        pass
