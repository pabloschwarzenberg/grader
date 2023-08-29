saldo_inicial = 1000000
saldo_cajero = saldo_inicial
usuario_valido = 10334151
clave_valida = 1803
intentos_fallidos = 0

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        saldo_usuario = 100000
        print("Bienvenido al cajero automático.")
        break
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            exit()
        else:
            print("Clave inválida. Por favor, inténtelo nuevamente.")

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido.")
    elif monto_retiro > saldo_usuario or monto_retiro > saldo_cajero:
        print("Saldo insuficiente.")
    else:
        saldo_usuario -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_usuario)
        print("Saldo cajero =", saldo_cajero)

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break
