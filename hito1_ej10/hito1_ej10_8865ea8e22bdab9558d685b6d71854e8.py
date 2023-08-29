#Cajero Automático
saldo_cajero = 1000000
saldo_inicial_usuario = 100000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        saldo_usuario = saldo_inicial_usuario
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada. Ha excedido el número de intentos.")
            exit()
        else:
            print("Clave inválida. Intente nuevamente.")

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido.")
        continue

    if monto > saldo_usuario:
        print("Saldo insuficiente. Su saldo actual es:", saldo_usuario)
    else:
        saldo_usuario -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_usuario)
        print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otra transacción? (N para salir): ")
    if opcion.upper() == "N":
        break    