def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            saldo_cuenta_usuario = saldo_cuenta
            intentos = 0
            break
        else:
            print("Usuario o clave incorrectos.")
            intentos += 1

        if intentos == 3:
            print("Tarjeta bloqueada.")
            return

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_cuenta_usuario:
            print("Saldo insuficiente.")
        elif monto > saldo_cajero:
            print("El cajero no tiene suficiente dinero para realizar el retiro.")
        else:
            saldo_cuenta_usuario -= monto
            saldo_cajero -= monto
            print("Saldo cuenta =", saldo_cuenta_usuario)
            print("Saldo cajero =", saldo_cajero)

        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()
