saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("¡Bienvenido!")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada. Por favor, comuníquese con el banco.")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta and monto_retiro > 0:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("saldo cuenta={}".format(saldo_cuenta))
        print("saldo cajero={}".format(saldo_cajero))
    elif monto_retiro <= 0:
        print("Monto no permitido. Por favor, ingrese un monto válido.")
    else:
        print("Fondos insuficientes. Por favor, ingrese un monto menor.")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break