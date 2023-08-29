saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_str = raw_input("Ingrese el monto a retirar: ")

    if monto_str.upper() == "N":
        break

    try:
        monto = int(monto_str)
    except ValueError:
        print("Monto no válido.")
        continue

    if monto <= 0:
        print("Monto no permitido.")
        continue
    elif monto > saldo_cuenta:
        print("Saldo insuficiente.")
        continue
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

print("Gracias por utilizar el cajero.")