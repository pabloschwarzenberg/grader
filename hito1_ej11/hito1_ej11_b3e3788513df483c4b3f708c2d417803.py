saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        break

    intentos += 1
    if intentos >= 3:
        print("Tarjeta bloqueada")
        exit()

    print("Clave inválida")
    print()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente")
    elif monto > sum(saldo_cajero.keys()):
        print("Cajero sin fondos suficientes")
    else:
        billetes_entregados = {}
        for denominacion in sorted(saldo_cajero.keys(), reverse=True):
            cantidad_billetes = min(monto // denominacion, saldo_cajero[denominacion])
            if cantidad_billetes > 0:
                billetes_entregados[denominacion] = cantidad_billetes
                monto -= denominacion * cantidad_billetes
                saldo_cajero[denominacion] -= cantidad_billetes

        if monto == 0:
            saldo_cuenta -= monto
            print("Retiro exitoso")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", sum(denominacion * saldo_cajero[denominacion] for denominacion in saldo_cajero.keys()))
            print("Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                print("billetes", denominacion, "=", cantidad)
        else:
            print("No se puede entregar el monto solicitado")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break