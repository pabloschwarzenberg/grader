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
        print("Bienvenido/a")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente")
    else:
        billetes_entregados = {}
        saldo_cuenta -= monto

        for denominacion in sorted(saldo_cajero.keys(), reverse=True):
            cantidad_disponible = saldo_cajero[denominacion]
            billetes_necesarios = min(monto // denominacion, cantidad_disponible)

            if billetes_necesarios > 0:
                billetes_entregados[denominacion] = billetes_necesarios
                monto -= billetes_necesarios * denominacion
                saldo_cajero[denominacion] -= billetes_necesarios

            if monto == 0:
                break

        if monto > 0:
            print("No se pueden entregar los billetes exactos")
            saldo_cuenta += monto

        print("Retiro exitoso")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        print("Billetes entregados:")
        for denominacion, cantidad in billetes_entregados.items():
            print("Billetes", denominacion, "=", cantidad)

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar.upper() != "S":
        break
