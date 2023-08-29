#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        print("Clave inválida.")

        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido.")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente.")
    elif monto > saldo_cajero:
        print("Cajero sin suficiente efectivo.")
    else:
        saldo_cuenta = monto
        saldo_cajero = monto
        print(f"Retiro exitoso. Saldo cuenta: {saldo_cuenta}. Saldo cajero: {saldo_cajero}")

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break
