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
        print("Acceso permitido")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= saldo_cuenta and monto <= saldo_cajero:
        # Calcula la cantidad de billetes de cada denominación a entregar
        billetes_20000_entregados = min(monto // 20000, billetes_20000)
        monto -= billetes_20000_entregados * 20000

        billetes_10000_entregados = min(monto // 10000, billetes_10000)
        monto -= billetes_10000_entregados * 10000

        billetes_5000_entregados = min(monto // 5000, billetes_5000)
        monto -= billetes_5000_entregados * 5000

        saldo_cuenta -= (billetes_20000_entregados * 20000 + billetes_10000_entregados * 10000 + billetes_5000_entregados * 5000)
        saldo_cajero -= (billetes_20000_entregados * 20000 + billetes_10000_entregados * 10000 + billetes_5000_entregados * 5000)

        print(f"Saldo cuenta: {saldo_cuenta}")
        print(f"Saldo cajero: {saldo_cajero}")
        print(f"Billetes 20000: {billetes_20000_entregados}")
        print(f"Billetes 10000: {billetes_10000_entregados}")
        print(f"Billetes 5000: {billetes_5000_entregados}")

    else:
        print("Monto no permitido")

    opcion = input("¿Desea realizar otra operación? (S/N): ")
    if opcion.upper() != "S":
        break
