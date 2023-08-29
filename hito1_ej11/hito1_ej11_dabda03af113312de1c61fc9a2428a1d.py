def cajero():
    billetes_20000 = 20
    billetes_10000 = 40
    billetes_5000 = 40
    saldo_cajero = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000
    saldo_cuenta = 100000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            intentos = 0
            print("Acceso permitido\n")

            while True:
                monto_retiro = float(input("Ingrese el monto a retirar: "))

                if monto_retiro > saldo_cuenta:
                    print("Monto no permitido. El saldo de su cuenta es insuficiente.\n")
                elif monto_retiro > saldo_cajero:
                    print("Monto no permitido. El cajero no cuenta con suficiente dinero.\n")
                else:
                    # Cálculo de billetes
                    billetes_20000_retirados = min(monto_retiro // 20000, billetes_20000)
                    monto_retiro -= billetes_20000_retirados * 20000

                    billetes_10000_retirados = min(monto_retiro // 10000, billetes_10000)
                    monto_retiro -= billetes_10000_retirados * 10000

                    billetes_5000_retirados = min(monto_retiro // 5000, billetes_5000)
                    monto_retiro -= billetes_5000_retirados * 5000

                    saldo_cuenta -= (billetes_20000_retirados * 20000 +
                                     billetes_10000_retirados * 10000 +
                                     billetes_5000_retirados * 5000)
                    saldo_cajero -= (billetes_20000_retirados * 20000 +
                                     billetes_10000_retirados * 10000 +
                                     billetes_5000_retirados * 5000)

                    # Impresión de resultados
                    print("\nRetiro exitoso.")
                    print("Saldo cuenta:", saldo_cuenta)
                    print("Saldo cajero:", saldo_cajero)

                    print("\nBilletes entregados:")
                    print("Billetes 20000:", billetes_20000_retirados)
                    print("Billetes 10000:", billetes_10000_retirados)
                    print("Billetes 5000:", billetes_5000_retirados, "\n")
        else:
            intentos += 1
            print("Clave inválida. Intento:", intentos, "\n")

            if intentos == 3:
                print("Tarjeta bloqueada. Ha excedido el número máximo de intentos.")
                break

        opcion = input("¿Desea realizar otra transacción? (N para salir): ")
        if opcion.upper() == "N":
            break

cajero()
      