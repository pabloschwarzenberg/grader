#Cajero Automático
def cajero():
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }

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
                else:
                    billetes_entregados = {}

                    for denominacion, cantidad in saldo_cajero.items():
                        if monto_retiro >= denominacion:
                            cantidad_entregada = min(monto_retiro // denominacion, cantidad)
                            monto_retiro -= cantidad_entregada * denominacion
                            saldo_cajero[denominacion] -= cantidad_entregada
                            billetes_entregados[denominacion] = cantidad_entregada

                    if monto_retiro > 0:
                        print("Monto no permitido. No se pueden entregar billetes para el monto solicitado.")
                    else:
                        saldo_usuario -= monto_retiro
                        print("Retiro exitoso.")
                        print("Saldo cuenta:", saldo_usuario)
                        print("Saldo cajero:", saldo_cajero)
                        print("Billetes entregados:")
                        for denominacion, cantidad_entregada in billetes_entregados.items():
                            print("Billetes", denominacion, "=", cantidad_entregada)

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
      