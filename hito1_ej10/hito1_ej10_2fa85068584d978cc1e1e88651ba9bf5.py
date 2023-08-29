#Cajero Automático
def cajero(usuario, clave, monto_retiro):
    # Datos del usuario y saldo inicial
    usuario_valido = "10334151"
    clave_valida = "1803"
    saldo_inicial = 1000000

    # Contadores de intentos fallidos y bloqueo
    intentos_fallidos = 0
    bloqueado = False

    # Validar usuario y clave
    if usuario == usuario_valido and clave == clave_valida:
        print("Ingreso exitoso")
        saldo = saldo_inicial
        intentos_fallidos = 0
        bloqueado = False

        # Mostrar saldo inicial
        print("Saldo inicial de la cuenta:", saldo)

        # Validar monto y realizar retiro
        if monto_retiro <= 0:
            print("Monto no permitido")
        elif monto_retiro > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= monto_retiro
            print("Retiro exitoso. Nuevo saldo de la cuenta:", saldo)

        # Mostrar saldo actualizado y saldo del cajero
        saldo_cajero = saldo_inicial - saldo
        print("Saldo actual de la cuenta:", saldo)
        print("Saldo del cajero:", saldo_cajero)

    else:
        intentos_fallidos += 1
        print("Clave inválida")

        if intentos_fallidos >= 3:
            bloqueado = True
            print("Tarjeta bloqueada")

    return saldo, saldo_cajero


if __name__ == "__main__":
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    saldo_final, saldo_cajero_final = cajero(usuario, clave, monto_retiro)

    print("Saldo final de la cuenta:", saldo_final)
    print("Saldo final del cajero:", saldo_cajero_final)