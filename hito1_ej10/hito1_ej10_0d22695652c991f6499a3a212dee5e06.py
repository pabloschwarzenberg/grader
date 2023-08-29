saldo_inicial = 1000000
saldo_cuenta = 100000
intentos_fallidos = 0
clave_valida = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        clave_valida = True
        break
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada. Ha excedido el número de intentos.")
            exit()
        else:
            print("Clave inválida. Por favor, intente nuevamente.")

while True:
    try:
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_cuenta:
            print("Saldo insuficiente. Su saldo actual es:", saldo_cuenta)
        else:
            saldo_cuenta -= monto
            saldo_cajero = saldo_inicial - saldo_cuenta
            print("Retiro exitoso. Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)

        opcion = input("¿Desea realizar otro retiro? (N para salir): ")
        if opcion.upper() == "N":
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

