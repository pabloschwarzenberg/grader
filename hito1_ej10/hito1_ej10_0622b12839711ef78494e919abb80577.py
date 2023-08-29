saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input('Ingrese su número de usuario: '))
    clave = int(input('Ingrese su clave: '))

    if usuario == usuario_valido and clave == clave_valida:
        print('acceso permitido')
        break
    else:
        intentos_fallidos += 1
        print('clave invalida')

        if intentos_fallidos >= 3:
            print('tarjeta bloqueada')
            exit()

while True:
    monto_retiro = int(input('Ingrese el monto a retirar: '))

    if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print('saldo cuenta=', saldo_cuenta, ',', 'saldo cajero=', saldo_cajero)
        break
    else:
        print('monto no permitido')
