saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

billetes_disponibles = {
    20000: 20,
    10000: 40,
    5000: 40
}

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
        billetes_entregados = {}
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro

        for billete, cantidad_disponible in billetes_disponibles.items():
            cantidad_billetes = min(monto_retiro // billete, cantidad_disponible)
            monto_retiro -= cantidad_billetes * billete
            billetes_entregados[billete] = cantidad_billetes
            billetes_disponibles[billete] -= cantidad_billetes

        print('saldo cuenta=', saldo_cuenta, ',', 'saldo cajero=', saldo_cajero)
        
        for billete, cantidad_entregada in billetes_entregados.items():
            print('billetes', billete, '=', cantidad_entregada)
        break
    else:
        print('monto no permitido')