saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido(a) al cajero.")
        break
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido.")
    elif monto_retiro > saldo_cuenta:
        print("Saldo insuficiente.")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
