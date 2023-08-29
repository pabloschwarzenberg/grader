#Cajero Automático
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

saldo_cuenta = 100000
saldo_cajero = billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000

intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        intentos_fallidos = 0

        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro > saldo_cajero:
                print("Monto no permitido. El cajero no tiene suficiente saldo.")
            else:
                billetes_20000_retirados = min(billetes_20000, int(monto_retiro / 20000))
                monto_retiro -= billetes_20000_retirados * 20000
                billetes_10000_retirados = min(billetes_10000, int(monto_retiro / 10000))
                monto_retiro -= billetes_10000_retirados * 10000
                billetes_5000_retirados = min(billetes_5000, int(monto_retiro / 5000))
                monto_retiro -= billetes_5000_retirados * 5000

                if monto_retiro > 0:
                    print("Monto no permitido. No se puede entregar la cantidad exacta de billetes.")
                else:
                    saldo_cuenta -= (billetes_20000_retirados * 20000 +
                                     billetes_10000_retirados * 10000 +
                                     billetes_5000_retirados * 5000)
                    saldo_cajero -= (billetes_20000_retirados * 20000 +
                                     billetes_10000_retirados * 10000 +
                                     billetes_5000_retirados * 5000)

                    print("Retiro exitoso.")
                    print("Saldo cuenta =", saldo_cuenta)
                    print("Saldo cajero =", saldo_cajero)
                    print("Billetes 20000 =", billetes_20000_retirados)
                    print("Billetes 10000 =", billetes_10000_retirados)
                    print("Billetes 5000 =", billetes_5000_retirados)

            opcion_continuar = input("¿Desea realizar otro retiro? (S/N): ")

            if opcion_continuar.upper() != "S":
                break

        break

    else:
        print("Clave inválida.")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada. Ha alcanzado el límite de intentos fallidos.")
            break

      