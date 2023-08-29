saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

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
    except EOFError:
        print("Error al leer el monto. Intente nuevamente.")
        continue

    if monto_retiro <= 0:
        print("Monto no permitido. Ingrese un monto válido.")
    elif monto_retiro > saldo_cuenta:
        print("Saldo insuficiente en la cuenta. Ingrese un monto menor.")
    elif monto_retiro > saldo_cajero:
        print("El cajero no tiene suficiente dinero. Ingrese un monto menor.")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("saldo cuenta=" + str(saldo_cuenta))
        print("saldo cajero=" + str(saldo_cajero))

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion != "S":
        break

    if opcion != "S":
        break
