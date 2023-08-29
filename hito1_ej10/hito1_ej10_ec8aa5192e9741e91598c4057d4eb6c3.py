saldo_inicial = 1000000
saldo_cajero = 1000000
intentos_fallidos = 0
usuario_valido = "10334151"
clave_valida = "1803"
saldo_usuario = 100000

while True:
    usuario = usuario_valido
    clave = clave_valida

    if usuario == usuario_valido and clave == clave_valida:
        print("Bienvenido/a,", usuario)

        monto_retiro = 45000  # Modifica este valor según tus necesidades

        if monto_retiro > saldo_usuario or monto_retiro <= 0:
            print("Monto no permitido")
        else:
            saldo_usuario -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_cajero)

        opcion = input("¿Desea realizar otro retiro? (N para salir): ")
        if opcion.upper() != "N":
            break

    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
