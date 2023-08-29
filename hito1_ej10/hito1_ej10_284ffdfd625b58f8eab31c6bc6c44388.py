saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial

continuar = True

while continuar:
    intentos = 0
    usuario_valido = False

    while intentos < 3 and not usuario_valido:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            usuario_valido = True
        else:
            print("Usuario o clave incorrectos. Intente nuevamente.")
            intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada.")
        break

    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta:
        if monto_retiro <= saldo_cajero:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro

            print("Retiro exitoso.")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)
        else:
            print("Monto no permitido. Fondos insuficientes en el cajero.")
    else:
        print("Monto no permitido. Fondos insuficientes en la cuenta.")

    respuesta = input("¿Desea realizar otra transacción? (S/N): ")
    if respuesta.upper() != "S":
        continuar = False
