#Cajero Automático
saldo_inicial = 1000000
saldo_cajero = saldo_inicial
intentos_fallidos = 0
usuario_valido = 10334151
clave_valida = 1803
saldo_usuario = 100000

while intentos_fallidos < 3:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_usuario:
            if monto_retiro <= saldo_cajero:
                saldo_usuario -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso.")
                print("Saldo cuenta:", saldo_usuario)
                print("Saldo cajero:", saldo_cajero)
            else:
                print("Monto no permitido. Fondos insuficientes en el cajero.")
        else:
            print("Monto no permitido. Fondos insuficientes en la cuenta.")
    else:
        intentos_fallidos += 1
        print("Clave inválida. Intentos fallidos:", intentos_fallidos)

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        break
     