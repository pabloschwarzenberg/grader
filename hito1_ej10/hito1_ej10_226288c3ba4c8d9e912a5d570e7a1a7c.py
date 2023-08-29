saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario != usuario_valido or clave != clave_valida:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada.")
            break
    else:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro > saldo_cuenta or monto_retiro <= 0:
            print("Monto no permitido.")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro

            print("saldo cuenta=" + str(saldo_cuenta))
            print("saldo cajero=" + str(saldo_cajero))

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break