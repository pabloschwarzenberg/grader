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
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            exit()
        else:
            print("Clave inválida. Intente nuevamente.")

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("Saldo cuenta=", saldo_cuenta)
        print("Saldo cajero=", saldo_cajero)
    else:
        print("Monto no permitido.")

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion != "S":
        break
