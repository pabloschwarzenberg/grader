saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido/a")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso")
        print("Saldo cuenta=" + str(saldo_cuenta))
        print("Saldo cajero=" + str(saldo_cajero))

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar.upper() != "S":
        break
