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
        print("Acceso concedido.\n")
        break
    else:
        print("Acceso denegado.\n")
        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido.\n")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente.\n")
    else:
        billetes_retirados = {
            20000: 0,
            10000: 0,
            5000: 0
        }

        for billete in saldo_cajero:
            cantidad_billetes = min(monto // billete, saldo_cajero[billete])
            monto -= billete * cantidad_billetes
            saldo_cajero[billete] -= cantidad_billetes
            billetes_retirados[billete] = cantidad_billetes

        saldo_cuenta -= (monto - (monto % 1000))
        saldo_cajero[1000] += (monto % 1000) // 1000

        print("Retiro exitoso.")
        print("Saldo cuenta: ", saldo_cuenta)
        print("Saldo cajero: ", saldo_cajero)
        print("Billetes retirados:")
        for billete, cantidad in billetes_retirados.items():
            print("billetes", billete, "=", cantidad)
        print()

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break
