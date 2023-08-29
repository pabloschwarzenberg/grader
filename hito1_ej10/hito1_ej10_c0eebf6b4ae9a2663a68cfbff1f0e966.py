#Cajero Automático
SALDO_CAJERO =  1000000
SALDO_USUARIO = 100000
intentos = 3
usuario = int(input("Ingresa ID usuario: "))
while True:
    clave = int(input("Ingresa clave: "))
    if clave == 1803:
        print('retirar ')
        monto = int(input('Ingrese monto: '))
        if monto <= SALDO_USUARIO:
            x = SALDO_USUARIO - monto
            y = SALDO_CAJERO - x + 10000
            print('saldo cuenta = ',x)
            print('saldo cajero =',y)
        else:
            print('monto no permitido')
        break
    else:
        intentos -=1
        if intentos == 0:
            print("Tarjeta Bloqueada")
            break