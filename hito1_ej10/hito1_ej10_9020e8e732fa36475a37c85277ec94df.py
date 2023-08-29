saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while intentos_fallidos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_usuario:
            saldo_usuario -= monto_retiro
            saldo_inicial -= monto_retiro

            print("Retiro exitoso.")
            print("Nuevo saldo en la cuenta corriente:", saldo_inicial)
            print("Nuevo saldo en el cajero:", saldo_usuario)
        else:
            print("Monto no permitido.")
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
