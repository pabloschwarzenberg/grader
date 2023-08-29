def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            intentos = 0
            print("Acceso permitido\n")

            while True:
                monto_retiro = (input("Ingrese el monto a retirar: "))

                if monto_retiro > saldo_cuenta:
                    print("Monto no permitido. El saldo de su cuenta es insuficiente.\n")
                elif monto_retiro > saldo_cajero:
                    print("Monto no permitido. El cajero no cuenta con suficiente dinero.\n")
                else:
                    saldo_cuenta -= monto_retiro
                    saldo_cajero -= monto_retiro
                    print("Retiro exitoso.")
                    print("Saldo cuenta:", saldo_cuenta)
                    print("Saldo cajero:", saldo_cajero, "\n")
        else:
            intentos += 1
            print("Clave inválida. Intento:", intentos, "\n")

            if intentos == 3:
                print("Tarjeta bloqueada. Ha excedido el número máximo de intentos.")
                break

        opcion = input("¿Desea realizar otra transacción? (N para salir): ")
        if opcion.upper() == "N":
            break

cajero()

      