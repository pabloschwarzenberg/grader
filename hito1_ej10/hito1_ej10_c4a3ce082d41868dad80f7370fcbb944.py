saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0
usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_usuario:
                saldo_usuario -= monto_retiro
                saldo_inicial -= monto_retiro
                print("Retiro exitoso.")
                print("Nuevo saldo en su cuenta corriente:", saldo_usuario)
                print("Nuevo saldo en el cajero:", saldo_inicial)
                break
            else:
                print("Monto no permitido. Fondos insuficientes.")

        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada. Contacte al servicio al cliente.")
            break
