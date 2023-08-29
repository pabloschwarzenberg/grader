#Cajero Automático
def cajero():
    saldo_cajero = 1000000
    usuario_valido = "10334151"
    clave_valida = "1803"
    saldo_usuario = 100000
    intentos_fallidos = 0

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == usuario_valido and clave == clave_valida:
            while True:
                monto_retiro = float(input("Ingrese el monto a retirar: "))

                if monto_retiro > saldo_usuario:
                    print("Monto no permitido. Saldo insuficiente en la cuenta.")
                elif monto_retiro > saldo_cajero:
                    print("Monto no permitido. Saldo insuficiente en el cajero.")
                else:
                    saldo_usuario -= monto_retiro
                    saldo_cajero -= monto_retiro
                    print("Retiro exitoso.")
                    print("Saldo cuenta:", saldo_usuario)
                    print("Saldo cajero:", saldo_cajero)
                    break
        else:
            intentos_fallidos += 1
            print("Clave inválida.")
            if intentos_fallidos == 3:
                print("Tarjeta bloqueada.")
                break

        continuar = input("¿Desea realizar otra transacción? (N para salir): ")
        if continuar.upper() == "N":
            break

cajero()