def cajero():
    saldo_cuenta = 100000
    saldo_total = 1000000
    saldo_cajero = {20000: 20, 10000: 40, 5000: 40}

    intentos = 0

    while True:
        usuario = '10334151'
        clave = '1803'
        print('')

        if usuario == '10334151' and clave == '1803':
            print('Inicio de sesión exitoso.')
            print('')
            print('BIENVENIDO')
            saldo_usuario = saldo_cuenta
            print('')
            break

        else:
            print('Usuario o clave inválidos.')
            intentos += 1
            print('')

            if intentos == 3:
                print('TARJETA BLOQUEADA')
                return

    while True:
        monto=int(input(len('Ingrese el retiro: ')))
        print('')

        if monto > saldo_usuario:
            print('Monto no permitido. Fondos insuficientes.')
            print('')

        elif monto > sum(k * v for k, v in saldo_cajero.items()):
            print('Monto no permitido. Cajero sin suficiente dinero.')
            print('')

        else:
            billetes_entregados = {}
            saldo_usuario -= monto

            for billete, cantidad in sorted(saldo_cajero.items(), reverse=True):
                if monto >= billete and cantidad > 0:
                    cantidad_entregada = min(monto // billete, cantidad)
                    billetes_entregados[billete] = cantidad_entregada
                    monto -= billete * cantidad_entregada
                    saldo_cajero[billete] -= cantidad_entregada

            if monto == 0:
              print('Retiro exitoso.')
              print('')
              print('Saldo cuenta =', saldo_usuario)
              print('')

              print('Billetes entregados:')
              for billete, cantidad_entregada in billetes_entregados.items():
                  print('Billetes', billete, '=', cantidad_entregada)
                  print('')

            else:
                print('Monto no permitido. No es posible entregar la cantidad exacta con los billetes disponibles.')
                print('')

        opcion = input('¿Desea realizar otro retiro? (S/N): ')
        print('')

        if opcion.upper() == 'N':
            break

cajero()
