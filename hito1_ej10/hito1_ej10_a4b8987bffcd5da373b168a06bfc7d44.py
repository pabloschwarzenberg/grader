#Cajero Automático
def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos_fallidos = 0

    usuario_valido = 10334151
    clave_valida = 1803

    while True:
        usuario = int(input("Ingrese su usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            print("¡Bienvenido!")
            break
        else:
            intentos_fallidos += 1
            if intentos_fallidos == 3:
                print("Tarjeta bloqueada. Intente más tarde.")
                return
            else:
                print("Clave inválida. Intente nuevamente.")

    while True:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
        elif monto_retiro > saldo_cuenta:
            print("Monto no permitido. Fondos insuficientes en la cuenta.")
        elif monto_retiro > saldo_cajero:
            print("Monto no permitido. Fondos insuficientes en el cajero.")
        else:
            print("Monto no permitido.")

        respuesta = input("¿Desea realizar otro retiro? (S/N): ")
        if respuesta.upper() != "N":
            break


cajero()
      