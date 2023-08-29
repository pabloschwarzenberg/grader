def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            saldo_inicial_usuario = 100000
            break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada")
                return

            print("Clave inválida. Intente nuevamente.")

    print("Bienvenido, usuario")

    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido")
        elif monto > saldo_cuenta:
            print("Saldo insuficiente")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

        opcion = input("¿Desea realizar otra transacción? (S/N): ")
        if opcion.lower() != "s":
            break

cajero()
