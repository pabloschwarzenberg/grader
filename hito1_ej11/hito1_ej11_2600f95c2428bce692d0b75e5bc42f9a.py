saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

intentos = 0
bloqueado = False

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        if intentos == 3:
            bloqueado = True
            print("Tarjeta bloqueada.")
            break
        else:
            print("Clave inválida. Intente nuevamente.")

while not bloqueado:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0 or monto > saldo_cuenta:
        print("Monto no permitido.")
    else:
        billetes_entregados = {}
        saldo_temporal = saldo_cajero.copy()
        for denominacion in sorted(saldo_temporal.keys(), reverse=True):
            cantidad_billetes = min(int(monto / denominacion), saldo_temporal[denominacion])
            billetes_entregados[denominacion] = cantidad_billetes
            monto -= cantidad_billetes * denominacion
            saldo_temporal[denominacion] -= cantidad_billetes

        if monto == 0:
            saldo_cuenta -= monto
            saldo_cajero = saldo_temporal

            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                print("billetes", denominacion, "=", cantidad)
        else:
            print("No se pueden entregar los billetes para el monto solicitado.")

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar.upper() != "S":
        break
