saldo_cuenta = 100000
saldo_cajero = 1000000

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos = 0
usuario = 10334151
clave = 1803

while True:
    input_usuario = int(input("Ingrese su usuario: "))
    input_clave = int(input("Ingrese su clave: "))

    if input_usuario == usuario and input_clave == clave:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta:
            if monto_retiro <= saldo_cajero:
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

                print("Saldo cuenta=", saldo_cuenta)
                print("Saldo cajero=", saldo_cajero)
                print("Billetes 20000=", billetes_20000_retirados)
                print("Billetes 10000=", billetes_10000_retirados)
                print("Billetes 5000=", billetes_5000_retirados)
            else:
                print("Monto no permitido. No hay suficiente dinero en el cajero.")
        else:
            print("Monto no permitido. No tiene suficiente saldo en su cuenta.")

    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            break
        else:
            print("Clave inválida. Intentos restantes:", 3 - intentos)

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break
