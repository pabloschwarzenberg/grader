def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            print("Acceso permitido")
            break
        else:
            intentos += 1
            if intentos == 3:
                print("Tarjeta bloqueada")
                return
            else:
                print("Clave inválida. Intente nuevamente.")

    while True:
        try:
            monto_retiro = int(input("Ingrese el monto a retirar: "))
            if monto_retiro <= 0:
                print("Monto no permitido. Intente nuevamente.")
            elif monto_retiro > saldo_cuenta:
                print("Saldo insuficiente. Intente nuevamente.")
            elif monto_retiro > saldo_cajero:
                print("Cajero sin fondos suficientes. Intente nuevamente.")
            else:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso.")
                print("Saldo cuenta:", saldo_cuenta)
                print("Saldo cajero:", saldo_cajero)
                break
        except ValueError:
            print("Ingrese un monto válido.")

    respuesta = input("¿Desea realizar otra transacción? (N para salir): ")
    if respuesta.upper() != "N":
        cajero()

cajero()

      