def cajero(usuario, clave, monto_retiro):
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    billetes_20000 = 20
    billetes_10000 = 40
    billetes_5000 = 40

    if usuario == "10334151" and clave == "1803":
        saldo_cuenta = 100000
        print("Bienvenido/a. Su saldo actual es:", saldo_cuenta)

        if monto_retiro <= 0:
            print("Monto no permitido.")
        elif monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
            print("Monto no permitido. Saldo insuficiente.")
        else:
            if monto_retiro > saldo_cajero:
                print("Monto no permitido. Cajero sin fondos suficientes.")
            else:
                # Distribución de billetes
                cantidad_20000 = min(monto_retiro // 20000, billetes_20000)
                monto_retiro -= cantidad_20000 * 20000
                billetes_20000 -= cantidad_20000

                cantidad_10000 = min(monto_retiro // 10000, billetes_10000)
                monto_retiro -= cantidad_10000 * 10000
                billetes_10000 -= cantidad_10000

                cantidad_5000 = min(monto_retiro // 5000, billetes_5000)
                monto_retiro -= cantidad_5000 * 5000
                billetes_5000 -= cantidad_5000

                # Actualización de saldos
                saldo_cuenta -= (monto_retiro + cantidad_20000 * 20000 + cantidad_10000 * 10000 + cantidad_5000 * 5000)
                saldo_cajero -= (cantidad_20000 * 20000 + cantidad_10000 * 10000 + cantidad_5000 * 5000)

                print("saldo cuenta={}".format(saldo_cuenta))
                print("saldo cajero={}".format(saldo_cajero))

                # Impresión de billetes entregados
                print("billetes 20000={}".format(cantidad_20000))
                print("billetes 10000={}".format(cantidad_10000))
                print("billetes 5000={}".format(cantidad_5000))

    else:
        intentos += 1
        print("Clave inválida.")

        if intentos == 3:
            print("Tarjeta bloqueada.")

# Ejemplo de uso
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")
monto_retiro = int(input("Ingrese el monto a retirar: "))

cajero(usuario, clave, monto_retiro)