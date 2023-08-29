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
        print("Inicio de sesión exitoso")
        break
    else:
        print("Clave inválida")
        intentos += 1

        if intentos == 3:
            print("Tarjeta bloqueada")
            exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido")
    else:
        billetes_entregados = {
            20000: 0,
            10000: 0,
            5000: 0
        }

        monto_disponible = sum(billete * cantidad for billete, cantidad in saldo_cajero.items())
        if monto > monto_disponible:
            print("Monto no permitido")
            continue

        # Distribuir el monto en los billetes disponibles
        for billete in sorted(saldo_cajero, reverse=True):
            cantidad_billetes = min(monto // billete, saldo_cajero[billete])
            monto -= billete * cantidad_billetes
            saldo_cajero[billete] -= cantidad_billetes
            billetes_entregados[billete] = cantidad_billetes

        if monto == 0:
            saldo_cuenta -= sum(billete * cantidad for billete, cantidad in billetes_entregados.items())
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

            # Imprimir la cantidad de billetes entregados
            print("Billetes entregados:")
            for billete, cantidad in billetes_entregados.items():
                if cantidad > 0:
                    print("Billetes", billete, "=", cantidad)
        else:
            print("Monto no permitido")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
