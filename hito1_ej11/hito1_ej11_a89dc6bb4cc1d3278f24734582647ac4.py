saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0

usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

if usuario == "10334151" and clave == "1803":
    while intentos < 3:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= saldo_cuenta:
            if monto % 5000 != 0:
                print("Monto no permitido. Debe ser múltiplo de 5000.")
            elif monto > saldo_cajero:
                print("No hay suficiente dinero en el cajero.")
            else:
                billetes_20000_retirados = min(billetes_20000, monto // 20000)
                monto -= billetes_20000_retirados * 20000
                billetes_10000_retirados = min(billetes_10000, monto // 10000)
                monto -= billetes_10000_retirados * 10000
                billetes_5000_retirados = min(billetes_5000, monto // 5000)
                monto -= billetes_5000_retirados * 5000

                saldo_cuenta -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)
                saldo_cajero -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)

                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
                print("billetes 20000 =", int(billetes_20000_retirados))
                print("billetes 10000 =", int(billetes_10000_retirados))
                print("billetes 5000 =", int(billetes_5000_retirados))
                break
        else:
            print("Monto no permitido. Intente nuevamente.")
else:
    print("Clave inválida.")
    intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada.")
