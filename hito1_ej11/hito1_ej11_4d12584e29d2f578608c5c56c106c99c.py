saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido, usuario autorizado.")
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada. Intente nuevamente más tarde.")
            exit()
        else:
            print("Clave inválida. Intente nuevamente.")

while True:
    try:
        monto_retiro = float(input("Ingrese el monto a retirar: "))
    except ValueError:
        print("Error al leer el monto. Intente nuevamente.")
        continue

    if monto_retiro <= 0:
        print("Monto no permitido. Ingrese un monto válido.")
    elif monto_retiro > saldo_cuenta:
        print("Saldo insuficiente en la cuenta. Ingrese un monto menor.")
    elif monto_retiro > saldo_cajero:
        print("El cajero no tiene suficiente dinero. Ingrese un monto menor.")
    else:
        billetes_20000_retiro = min(monto_retiro // 20000, billetes_20000)
        monto_retiro -= billetes_20000_retiro * 20000
        billetes_10000_retiro = min(monto_retiro // 10000, billetes_10000)
        monto_retiro -= billetes_10000_retiro * 10000
        billetes_5000_retiro = min(monto_retiro // 5000, billetes_5000)
        monto_retiro -= billetes_5000_retiro * 5000

        if monto_retiro > 0:
            print("No se pueden entregar los billetes exactos para el monto solicitado.")

        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro

        print("Retiro exitoso.")
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)
        print("Billetes 20000:", billetes_20000_retiro)
        print("Billetes 10000:", billetes_10000_retiro)
        print("Billetes 5000:", billetes_5000_retiro)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion != "S":
        break
