def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos_fallidos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            print("Bienvenido(a) al cajero automático.")

            while True:
                monto = float(input("Ingrese el monto a retirar: "))

                if monto <= saldo_cuenta:
                    saldo_cuenta -= monto
                    saldo_cajero -= monto
                    print("Retiro exitoso.")
                    print("Saldo cuenta =", saldo_cuenta)
                    print("Saldo cajero =", saldo_cajero)
                else:
                    print("Monto no permitido. Saldo insuficiente en la cuenta.")

                continuar = input("¿Desea realizar otro retiro? (S/N): ")
                if continuar.upper() != "S":
                    break

            break
        else:
            intentos_fallidos += 1
            print("Clave inválida.")
            if intentos_fallidos == 3:
                print("Tarjeta bloqueada.")
                break

# Ejecutar el programa del cajero automático
cajero()

      