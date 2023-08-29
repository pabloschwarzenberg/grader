saldo_inicial = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos_fallidos = 0
clave_valida = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        clave_valida = True
        break
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada. Ha excedido el número de intentos.")
            exit()
        else:
            print("Clave inválida. Por favor, intente nuevamente.")

while True:
    try:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_inicial:
            print("Saldo insuficiente en el cajero.")
        else:
            billetes_retirados_20000 = min(billetes_20000, int(monto / 20000))
            monto -= billetes_retirados_20000 * 20000

            billetes_retirados_10000 = min(billetes_10000, int(monto / 10000))
            monto -= billetes_retirados_10000 * 10000

            billetes_retirados_5000 = min(billetes_5000, int(monto / 5000))
            monto -= billetes_retirados_5000 * 5000

            saldo_cajero = saldo_inicial - (billetes_retirados_20000 * 20000 + billetes_retirados_10000 * 10000 + billetes_retirados_5000 * 5000)
            saldo_inicial = saldo_cajero

            print("Retiro exitoso. Saldo cuenta:", saldo_inicial)
            print("Saldo cajero:", saldo_cajero)
            print("Billetes 20000:", billetes_retirados_20000)
            print("Billetes 10000:", billetes_retirados_10000)
            print("Billetes 5000:", billetes_retirados_5000)

        opcion = input("¿Desea realizar otro retiro? (N para salir): ")
        if opcion.upper() == "N":
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
