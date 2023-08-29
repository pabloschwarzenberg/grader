saldo_inicial_cuenta = 1000000
saldo_inicial_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos_fallidos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        saldo_cuenta = saldo_inicial_cuenta
        saldo_cajero = saldo_inicial_cajero
        billetes_entregados = {'20000': 0, '10000': 0, '5000': 0}

        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_cuenta:
                if monto_retiro <= saldo_cajero:
                    # Calcula la cantidad de billetes necesarios para cada denominación
                    cantidad_20000 = min(billetes_20000, int(monto_retiro / 20000))
                    monto_retiro -= cantidad_20000 * 20000
                    cantidad_10000 = min(billetes_10000, int(monto_retiro / 10000))
                    monto_retiro -= cantidad_10000 * 10000
                    cantidad_5000 = min(billetes_5000, int(monto_retiro / 5000))

                    if monto_retiro == 0:
                        # Actualiza los saldos y la cantidad de billetes
                        saldo_cuenta -= (cantidad_20000 * 20000) + (cantidad_10000 * 10000) + (cantidad_5000 * 5000)
                        saldo_cajero -= (cantidad_20000 * 20000) + (cantidad_10000 * 10000) + (cantidad_5000 * 5000)
                        billetes_20000 -= cantidad_20000
                        billetes_10000 -= cantidad_10000
                        billetes_5000 -= cantidad_5000

                        # Actualiza la cantidad de billetes entregados
                        billetes_entregados['20000'] = cantidad_20000
                        billetes_entregados['10000'] = cantidad_10000
                        billetes_entregados['5000'] = cantidad_5000

                        print("Retiro exitoso.")
                        print("Saldo cuenta =", saldo_cuenta)
                        print("Saldo cajero =", saldo_cajero)
                        print("Billetes entregados:")
                        for denominacion, cantidad in billetes_entregados.items():
                            print("billetes", denominacion, "=", cantidad)
                    else:
                        print("Monto no permitido. No hay suficiente cantidad de billetes.")
                else:
                    print("Monto no permitido. No hay suficiente dinero en el cajero.")
            else:
                print("Monto no permitido. No hay suficiente dinero en la cuenta.")

            continuar = input("¿Desea realizar otro retiro? (S/N): ")
            if continuar.upper() != "S":
                break

        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break