saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido.")
        continue
    elif monto_retiro > saldo_cuenta:
        print("Saldo insuficiente.")
        continue

    saldo_cuenta -= monto_retiro
    saldo_cajero -= monto_retiro

    print("Saldo cuenta = {}".format(saldo_cuenta))
    print("Saldo cajero = {}".format(saldo_cajero))

    respuesta = input("¿Desea realizar otro retiro? (N para salir): ")
    if respuesta.upper() == "N":
        break
