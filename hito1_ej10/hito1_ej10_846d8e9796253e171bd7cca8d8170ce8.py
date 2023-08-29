saldo_inicial = 1000000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        saldo_usuario = 100000
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0 or monto_retiro > saldo_usuario:
        print("Monto no permitido.")
    else:
        saldo_usuario -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Saldo cuenta=", saldo_usuario)
        print("Saldo cajero=", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
