saldo_cuenta = 100000
saldo_cajero = 1000000
billetes = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Ingreso exitoso.")
        break
    else:
        print("Clave invalida.")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido.")
        continue
    elif monto > saldo_cuenta or monto > saldo_cajero:
        print("Saldo insuficiente.")
        continue

    monto_restante = monto
    billetes_retirados = {}

    for denominacion, cantidad in billetes.items():
        if denominacion <= monto_restante and cantidad > 0:
            cantidad_retirada = min(monto_restante // denominacion, cantidad)
            monto_restante -= cantidad_retirada * denominacion
            billetes_retirados[denominacion] = cantidad_retirada
            billetes[denominacion] -= cantidad_retirada

    if monto_restante == 0:
        saldo_cuenta -= monto
        saldo_cajero -= monto

        print("Retiro exitoso.")
        print(f"Saldo cuenta: {saldo_cuenta}")
        print(f"Saldo cajero: {saldo_cajero}")
        for denominacion, cantidad_retirada in billetes_retirados.items():
            print(f"Billetes {denominacion}: {cantidad_retirada}")
    else:
        print("No es posible retirar el monto solicitado con los billetes disponibles.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() == "N":
        break
