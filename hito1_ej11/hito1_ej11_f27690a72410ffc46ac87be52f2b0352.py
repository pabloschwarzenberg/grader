def cajero_automatico():
    saldo_inicial = 1000000
    billetes_20000 = 20
    billetes_10000 = 40
    billetes_5000 = 40
    saldo_cajero = saldo_inicial

    intentos = 0
    usuario_valido = False

    while not usuario_valido and intentos < 3:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            usuario_valido = True
        else:
            print("Clave inválida.")
            intentos += 1

        if intentos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        if saldo_cajero == 0:
            print("Cajero sin saldo.")
            return

        if billetes_20000 == 0 and billetes_10000 == 0 and billetes_5000 == 0:
            print("Cajero sin billetes disponibles.")
            return

        if billetes_20000 > 0:
            max_billetes_20000 = min(saldo_cajero // 20000, billetes_20000)
        else:
            max_billetes_20000 = 0

        if billetes_10000 > 0:
            max_billetes_10000 = min(saldo_cajero // 10000, billetes_10000)
        else:
            max_billetes_10000 = 0

        if billetes_5000 > 0:
            max_billetes_5000 = min(saldo_cajero // 5000, billetes_5000)
        else:
            max_billetes_5000 = 0

        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cajero and monto_retiro <= (max_billetes_20000 * 20000 + max_billetes_10000 * 10000 + max_billetes_5000 * 5000):
            saldo_cajero -= monto_retiro

            billetes_retirados_20000 = min(monto_retiro // 20000, max_billetes_20000)
            monto_retiro -= billetes_retirados_20000 * 20000
            billetes_20000 -= billetes_retirados_20000

            billetes_retirados_10000 = min(monto_retiro // 10000, max_billetes_10000)
            monto_retiro -= billetes_retirados_10000 * 10000
            billetes_10000 -= billetes_retirados_10000

            billetes_retirados_5000 = min(monto_retiro // 5000, max_billetes_5000)
            monto_retiro -= billetes_retirados_5000 * 5000
            billetes_5000 -= billetes_retirados_5000

            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cajero)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes de 20000 =", billetes_retirados_20000)
            print("Billetes de 10000 =", billetes_retirados_10000)
            print("Billetes de 5000 =", billetes_retirados_5000)
        else:
            print("Monto no permitido. Saldo insuficiente en el cajero o no hay suficientes billetes para el monto solicitado.")

        opcion = input("¿Desea realizar otra transacción? (S/N): ")
        if opcion.upper() != "S":
            break

cajero_automatico()
