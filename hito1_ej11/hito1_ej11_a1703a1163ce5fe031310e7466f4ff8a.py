saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos = 0

while True:
    usuario = input('Ingrese el número de usuario: ')
    clave = input('Ingrese la clave: ')

    if usuario == '10334151' and clave == '1803':
        print('Inicio de sesión exitoso')
        break
    else:
        print('Clave inválida')
        intentos += 1

    if intentos == 3:
        print('Tarjeta bloqueada')
        exit()

while True:
    monto = float(input('Ingrese el monto a retirar: '))

    if monto <= saldo_cuenta:
        total_billetes = {}

        # Distribuir el monto en los billetes disponibles
        for billete in sorted(saldo_cajero.keys(), reverse=True):
            cantidad_billetes = min(monto // billete, saldo_cajero[billete])
            total_billetes[billete] = cantidad_billetes
            monto -= billete * cantidad_billetes
            saldo_cajero[billete] -= cantidad_billetes

        if monto == 0:
            saldo_cuenta -= monto
            print('Retiro exitoso')
            print('Saldo cuenta =', saldo_cuenta)
            print('Saldo cajero =', saldo_cajero)

            # Imprimir la cantidad de billetes entregados
            for billete, cantidad in total_billetes.items():
                if cantidad > 0:
                    print('billetes', billete, '=', cantidad)
        else:
            print('Monto no permitido: no hay suficientes billetes disponibles')
    else:
        print('Monto no permitido: saldo insuficiente en la cuenta')

    continuar = input('¿Desea realizar otra operación? (s/n): ')
    if continuar.lower() != 's':
        break
