#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("¡Bienvenido!")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta:
        print("Monto no permitido. Saldo insuficiente en la cuenta.")
    elif monto_retiro > saldo_cajero:
        print("Monto no permitido. Saldo insuficiente en el cajero.")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("saldo cuenta=" + str(saldo_cuenta))
        print("saldo cajero=" + str(saldo_cajero))

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar.upper() != "S":
        break

    