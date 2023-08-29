def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            saldo_usuario = saldo_cuenta
            break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada.")
                return
            else:
                print("Clave inválida.")

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_usuario:
            print("Saldo insuficiente.")
        elif monto > saldo_cajero:
            print("Cajero sin fondos suficientes.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

        opcion = input("¿Desea realizar otra transacción? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()
