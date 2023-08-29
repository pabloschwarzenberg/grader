#Cajero Automático
saldo_cuenta = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos = 0

while True:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()
        else:
            print("Clave inválida. Por favor intente nuevamente.")

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido. No cuenta con suficiente saldo.")
    elif monto > saldo_cuenta:
        print("Monto no permitido. El cajero no dispone de suficiente efectivo.")
    else:
        billetes_20000_retirados = min(billetes_20000, int(monto / 20000))
        monto -= billetes_20000_retirados * 20000
        billetes_10000_retirados = min(billetes_10000, int(monto / 10000))
        monto -= billetes_10000_retirados * 10000
        billetes_5000_retirados = min(billetes_5000, int(monto / 5000))
        monto -= billetes_5000_retirados * 5000

        saldo_cuenta -= (billetes_20000_retirados * 20000) + (billetes_10000_retirados * 10000) + (billetes_5000_retirados * 5000)
        billetes_20000 -= billetes_20000_retirados
        billetes_10000 -= billetes_10000_retirados
        billetes_5000 -= billetes_5000_retirados

        print(f"Retiro exitoso. Saldo en cuenta: {saldo_cuenta}, Saldo en cajero: {billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000}")
        print(f"Billetes 20000: {billetes_20000_retirados}")
        print(f"Billetes 10000: {billetes_10000_retirados}")
        print(f"Billetes 5000: {billetes_5000_retirados}")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
      