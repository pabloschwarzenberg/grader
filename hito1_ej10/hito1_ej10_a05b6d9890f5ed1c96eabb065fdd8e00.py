saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0
retiros_realizados = 0

while True:
    usuario = "10334151"
    clave = "1803"

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido, usuario 10334151")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada. Programa finalizado.")
            exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido. Fondos insuficientes en la cuenta.")
    elif monto > saldo_cajero:
        print("Monto no permitido. Fondos insuficientes en el cajero.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        retiros_realizados += 1

        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

    if retiros_realizados >= 3:
        print("Límite de retiros alcanzado. Programa finalizado.")
        break

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break
