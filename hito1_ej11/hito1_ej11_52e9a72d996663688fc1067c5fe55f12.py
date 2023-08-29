#Cajero Automático
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido, usuario 10334151.")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= 0 or monto > saldo_cuenta:
        print("Monto no permitido.")
    else:
        # Distribuir el monto en billetes
        billetes_20000_retirados = min(monto // 20000, billetes_20000)
        monto -= billetes_20000_retirados * 20000
        billetes_10000_retirados = min(monto // 10000, billetes_10000)
        monto -= billetes_10000_retirados * 10000
        billetes_5000_retirados = min(monto // 5000, billetes_5000)
        monto -= billetes_5000_retirados * 5000

        if monto > 0:
            print("No hay suficientes billetes para realizar el retiro.")
        else:
            saldo_cuenta -= (billetes_20000_retirados * 20000 +
                             billetes_10000_retirados * 10000 +
                             billetes_5000_retirados * 5000)
            saldo_cajero -= (billetes_20000_retirados * 20000 +
                             billetes_10000_retirados * 10000 +
                             billetes_5000_retirados * 5000)

            print("Retiro exitoso.")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)
            print("Billetes 20000:", billetes_20000_retirados)
            print("Billetes 10000:", billetes_10000_retirados)
            print("Billetes 5000:", billetes_5000_retirados)

    continuar = input("¿Desea realizar otro retiro? (N para salir): ")
    if continuar.upper() != "N":
        continue
    else:
        break
      