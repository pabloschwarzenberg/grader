saldo_cuenta = 100000
saldo_cajero = 1000000
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
        print("Tarjeta bloqueada. Ha excedido el número máximo de intentos.")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro

        print("Retiro exitoso.")
        print("saldo cuenta=" + str(saldo_cuenta))
        print("saldo cajero=" + str(saldo_cajero))
    else:
        print("Monto no permitido.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
