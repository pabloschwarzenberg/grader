def cajero():
    billetes_20000 = 20
    billetes_10000 = 40
    billetes_5000 = 40
    saldo_cajero = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000
    saldo_cuenta = 100000
    intentos = 0

    usuario_valido = 10334151
    clave_valida = 1803

    while True:
        usuario = int(input("Ingrese su número de usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            print("Inicio de sesión exitoso.")
            break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada. Demasiados intentos fallidos.")
                return
            print("Clave inválida. Intente nuevamente.")

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto > saldo_cuenta:
            print("Monto no permitido. No tiene suficiente saldo en su cuenta.")
        elif monto > saldo_cajero:
            print("Monto no permitido. El cajero no dispone de suficiente dinero.")
        else:
            billetes_20000_retirados = min(billetes_20000, int(monto // 20000))
            monto -= billetes_20000_retirados * 20000

            billetes_10000_retirados = min(billetes_10000, int(monto // 10000))
            monto -= billetes_10000_retirados * 10000

            billetes_5000_retirados = min(billetes_5000, int(monto // 5000))
            monto -= billetes_5000_retirados * 5000

            saldo_cuenta -= (billetes_20000_retirados * 20000 +
                             billetes_10000_retirados * 10000 +
                             billetes_5000_retirados * 5000)
            saldo_cajero -= (billetes_20000_retirados * 20000 +
                             billetes_10000_retirados * 10000 +
                             billetes_5000_retirados * 5000)

            print("Retiro exitoso.")
            print("Saldo en cuenta:", saldo_cuenta)
            print("Saldo en cajero:", saldo_cajero)
            print("Billetes de 20000:", billetes_20000_retirados)
            print("Billetes de 10000:", billetes_10000_retirados)
            print("Billetes de 5000:", billetes_5000_retirados)

        continuar = input("¿Desea realizar otra transacción? (S/N): ")
        if continuar != "S":
            break

cajero()
