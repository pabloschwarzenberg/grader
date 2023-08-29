def cajero():
    saldo_cuenta = 100000
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            saldo_usuario = saldo_cuenta
            break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada.")
                return
            else:
                print("Clave inválida.")

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_usuario:
            print("Saldo insuficiente.")
        elif monto > sum(saldo_cajero.keys()):
            print("Cajero sin fondos suficientes.")
        else:
            billetes_entregados = {}

            for billete, cantidad in saldo_cajero.items():
                billetes_entregados[billete] = min(int(monto / billete), cantidad)
                monto -= billetes_entregados[billete] * billete
                saldo_cajero[billete] -= billetes_entregados[billete]

            saldo_cuenta -= sum(billetes_entregados.values()) * 5000
            saldo_cajero_total = sum([billete * cantidad for billete, cantidad in saldo_cajero.items()])

            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero_total)

            for billete, cantidad in billetes_entregados.items():
                if cantidad > 0:
                    print("Billetes", billete, "=", cantidad)

        opcion = input("¿Desea realizar otra transacción? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()
