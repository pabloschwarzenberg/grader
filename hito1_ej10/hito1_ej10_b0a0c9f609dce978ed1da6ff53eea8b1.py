saldo_cajero = 1000000
saldo_usuario = 100000
intento = 0
letra_continuar = 'N'
usuario = input("usuario: ")
clave = input("contraseña: ")
while letra_continuar.upper() == 'N':
    if (clave == '1803' and usuario == '10334151'):
        monto_retiro = int(input("monto de retiro: "))
        if monto_retiro > saldo_usuario or monto_retiro > saldo_cajero:
            print("monto no permitido")
        else:
            saldo_cajero -= monto_retiro
            saldo_usuario -= monto_retiro
            print(['saldo cuenta=' + str(saldo_usuario), 'saldo cajero=' + str(saldo_cajero)])
            letra_continuar = input('para continuar presione la letra "N": ')
    else:
        intento += 1
        if intento >= 3:
            print("tarjeta bloqueada")
            letra_continuar = 'L'
        else:
            print("clave invalida")
            usuario = input("usuario: ")
            clave = input("clave: ")