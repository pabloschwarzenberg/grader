saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("¡Bienvenido!")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada. Por favor, comuníquese con el banco.")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta and monto_retiro > 0:
        billetes_entregados = {}
        monto_restante = monto_retiro

        for denominacion, cantidad in sorted(saldo_cajero.items(), reverse=True):
            if monto_restante >= denominacion and cantidad > 0:
                cantidad_billetes = min(monto_restante // denominacion, cantidad)
                monto_restante -= cantidad_billetes * denominacion
                saldo_cajero[denominacion] -= cantidad_billetes
                billetes_entregados[denominacion] = cantidad_billetes

        if monto_restante == 0:
            saldo_cuenta -= monto_retiro
            print("Retiro exitoso.")
            print("Saldo cuenta: {}".format(saldo_cuenta))
            print("Saldo cajero:")
            for denominacion, cantidad in saldo_cajero.items():
                print("Billetes de {}: {}".format(denominacion, cantidad))
            print("Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                print("Billetes de {}: {}".format(denominacion, cantidad))
        else:
            print("No se puede retirar la cantidad solicitada con los billetes disponibles.")
    elif monto_retiro <= 0:
        print("Monto no permitido. Por favor, ingrese un monto válido.")
    else:
        print("Fondos insuficientes. Por favor, ingrese un monto menor.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break