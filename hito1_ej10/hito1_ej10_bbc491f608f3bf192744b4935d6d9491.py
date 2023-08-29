#Cajero Automático
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

    if intentos >= 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    opcion = input("¿Desea realizar un retiro? (S/N): ")

    if opcion.upper() != "S":
        break

    monto = int(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido. Fondos insuficientes.")
    elif monto > saldo_cajero:
        print("Monto no permitido. Fondos insuficientes en el cajero.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)