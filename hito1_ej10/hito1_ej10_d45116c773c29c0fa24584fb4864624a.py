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
    monto = int(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta or monto < 0:
        print("Monto no permitido.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("saldo cuenta=" + str(saldo_cuenta))
        print("saldo cajero=" + str(saldo_cajero))

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar != "S":
        break
