saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

x = 'Y'
intentos = 0

while x.upper() != 'N':
    if intentos >= 3:
        print("Tarjeta bloqueada")
        break

    usuario = input("Ingrese usuario ('N' para salir): ")
    if usuario.upper() == 'N':
        x = 'N'
    elif usuario == '10334151':
        clave = input("Ingrese clave ('N' para salir): ")
        if clave.upper() == 'N':
            x = 'N'
        elif clave == '1803':
            while True:
                monto = input("¿Cuánto monto desea retirar? ('N' para salir): ")
                if monto.upper() == 'N':
                    x = 'N'
                    break
                else:
                    monto = int(monto)
                    if monto > sum(saldo_cajero.keys()):
                        print("Monto no permitido")
                    else:
                        billetes_entregados = {}
                        for denominacion, cantidad_disponible in saldo_cajero.items():
                            cantidad_billetes = min(monto // denominacion, cantidad_disponible)
                            billetes_entregados[denominacion] = cantidad_billetes
                            monto -= denominacion * cantidad_billetes
                            saldo_cajero[denominacion] -= cantidad_billetes

                        print("Billetes entregados:")
                        for denominacion, cantidad_billetes in billetes_entregados.items():
                            print(f"Billetes {denominacion} = {cantidad_billetes}")

                        print("Saldo cuenta =", sum(saldo_cajero.keys()))
                        print("Saldo cajero:")
                        for denominacion, cantidad_disponible in saldo_cajero.items():
                            print(f"Billetes {denominacion} = {cantidad_disponible}")

                        break
        else:
            print("Clave inválida")
            intentos += 1
    else:
        print("Usuario inválido")
        intentos += 1
