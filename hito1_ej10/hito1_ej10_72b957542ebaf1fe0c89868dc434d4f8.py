saldo_inicial = 1000000
saldo_cuenta = 100000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Acceso permitido")
        break
    else:
        intentos += 1
        print("Acceso denegado")

    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    opcion = input("¿Desea realizar un retiro? (S/N): ")

    if opcion.upper() != "S":
        break

    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido")
    else:
        # Distribución de billetes
        billetes_20000_retirados = min(billetes_20000, int(monto / 20000))
        monto -= billetes_20000_retirados * 20000

        billetes_10000_retirados = min(billetes_10000, int(monto / 10000))
        monto -= billetes_10000_retirados * 10000

        billetes_5000_retirados = min(billetes_5000, int(monto / 5000))
        monto -= billetes_5000_retirados * 5000

        # Actualización de saldos
        saldo_cuenta -= (billetes_20000_retirados * 20000) + (billetes_10000_retirados * 10000) + (billetes_5000_retirados * 5000)
        saldo_cajero = saldo_inicial - saldo_cuenta

        # Impresión de resultados
        print("saldo cuenta=" + str(saldo_cuenta))
        print("saldo cajero=" + str(saldo_cajero))

        # Actualización de billetes disponibles
        billetes_20000 -= billetes_20000_retirados
        billetes_10000 -= billetes_10000_retirados
        billetes_5000 -= billetes_5000_retirados

print("Gracias por utilizar el cajero automático")
