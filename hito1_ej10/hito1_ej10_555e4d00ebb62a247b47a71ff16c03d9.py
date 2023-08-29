saldo_inicial = 1000000
saldo_cajero = 1000000
intentos_fallidos = 0
usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        saldo_cuenta = 100000
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
    elif monto_retiro > saldo_cuenta:
        print("Monto no permitido. Saldo insuficiente en la cuenta.")
    elif monto_retiro > saldo_cajero:
        print("Monto no permitido. Saldo insuficiente en el cajero.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break